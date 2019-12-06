# 尝试使用模型
import numpy as np
import csv
import pickle

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

np.random.seed(1337)
n = 23291027


def save(data, filename):
    ff = open(filename, "wb")
    pickle.dump(data, ff)
    ff.close()


def load(filename):
    ff = open(filename, "rb")
    data = pickle.load(ff)
    ff.close()
    return data


class Big3:
    def __init__(self):
        self.one = 0.
        self.two = 0.
        self.three = 0.
        self.count = 0.

    def push(self, x):
        self.count += 1
        if x > self.one:
            self.three = self.two
            self.two = self.one
            self.one = x
        elif x > self.two:
            self.three = self.two
            self.two = x
        elif x > self.three:
            self.three = x

    def get_values(self):
        return self.one, self.two, self.three, self.count


def get_day(x):
    return (int(x[5:7]) - 11) * 30 + int(x[8:10]) - 18


def get_hour(x):
    return get_day(x) * 24 + int(x[11])


def init_buy_data():
    file = open("fresh_comp_offline/tianchi_fresh_comp_train_user.csv")
    actions = csv.reader(file)
    _ = next(actions)
    i = 0
    buy = [set()] * 31
    for row in actions:
        user_id = row[0]
        item_id = row[1]
        user_item = user_id + "," + item_id
        action = row[2]
        c = row[4]
        day = get_day(row[5])
        hour = get_hour(row[5])
        if action == "4":
            buy[day].add(user_item)
        i += 1
        if i % 200000 == 0:
            print("cal bought items progress: %.2f%%" % (i * 100 / n))

    file.close()
    return buy


def init_train_data(d, buy):
    print("train day %d" % d)
    file = open("fresh_comp_offline/tianchi_fresh_comp_train_user.csv")
    actions = csv.reader(file)
    _ = next(actions)
    users = {}
    i = 0
    for row in actions:
        user_id = row[0]
        item_id = row[1]
        user_item = user_id + "," + item_id
        action = int(row[2])
        c = int(row[4])
        day = get_day(row[5])
        hour = get_hour(row[5])
        if day >= d:
            i += 1
            continue
        if user_id not in users:
            users[user_id] = {item_id: [Big3(), Big3(), Big3(), Big3()]}
        if item_id not in users[user_id]:
            users[user_id][item_id] = [Big3(), Big3(), Big3(), Big3()]
        users[user_id][item_id][action - 1].push(10 / (d * 24 - hour))
        i += 1
        if i % 200000 == 0:
            print("prepare training data %.2f%%" % (100 * i / n))
    x = []
    y = []
    pairs = []
    print("process training data")
    for user_id in users:
        for item_id in users[user_id]:
            t = users[user_id][item_id]
            xx = []
            xx.extend(t[0].get_values())
            xx.extend(t[1].get_values())
            xx.extend(t[2].get_values())
            xx.extend(t[3].get_values())
            if (user_id + "," + item_id) in buy[d]:
                yy = 1
            else:
                yy = 0
            x.append(xx)
            y.append(yy)
            pairs.append(user_id + ',' + item_id)

    file.close()
    return x, y, pairs


def get_buy_data():
    filename = "buy_each_day.pickle"
    try:
        buy = load(filename)
        print("load data buy %d %d" % (len(buy), len(buy[0])))
    except FileNotFoundError:
        buy = init_buy_data()
        save(buy, filename)

    return buy


def get_train_data(d, buy):
    x_name = "x_%d.pickle" % d
    y_name = "y_%d.pickle" % d
    p_name = "p_%d.pickle" % d
    try:
        x = load(x_name)
        y = load(y_name)
        p = load(p_name)
    except FileNotFoundError:
        x, y, p = init_train_data(d, buy)
        save(x, x_name)
        save(y, y_name)
        save(p, p_name)
    return x, y, p


def write_result(result):
    print("write result")
    outfile = open("out3.csv", "w")
    for r in result:
        outfile.write(r + "\n")
    outfile.close()


clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=0)

buy = get_buy_data()
for d in range(29, 31):
    print("load date for %d" % d)
    x, y, p = get_train_data(d, buy)
    if d < 30:
        print("train...")
        clf.fit(x, y)
    if d == 30:
        print("predict...")
        y = clf.predict(x)
        result = []
        for i in range(len(x)):
            if y[i] > 0.5:
                result.append(p[i])
        write_result(result)
