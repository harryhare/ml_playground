# 尝试使用模型
# 倒数时间
import numpy as np
import csv
from big3 import *
from util import *
from counter import Counter

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

np.random.seed(1337)
n = 23291027


def init_buy_data():
    file = open("fresh_comp_offline/user_sorted_filtered.csv")
    actions = csv.reader(file)
    _ = next(actions)
    buy = []
    for j in range(32):
        buy.append(set())
    c = Counter(n, "calculate bought items")
    for row in actions:
        c.count_print()
        user_id = row[0]
        item_id = row[1]
        user_item = user_id + "," + item_id
        action = row[2]
        c = row[4]
        day = get_day(row[5])
        hour = get_hour(row[5])
        if action == "4":
            buy[day].add(user_item)

    file.close()
    return buy


def init_train_data(d, buy):
    print("train day %d" % d)
    file = open("fresh_comp_offline/user_sorted_filtered.csv")
    actions = csv.reader(file)
    _ = next(actions)
    users = {}
    c = Counter(n, "prepare training data")
    for row in actions:
        c.count_print()
        user_id = row[0]
        item_id = row[1]
        user_item = user_id + "," + item_id
        action = int(row[2])
        c = int(row[4])
        day = get_day(row[5])
        hour = get_hour(row[5])
        if day >= d:
            continue
        if user_id not in users:
            users[user_id] = {item_id: [Big3(), Big3(), Big3(), Big3()]}
        if item_id not in users[user_id]:
            users[user_id][item_id] = [Big3(), Big3(), Big3(), Big3()]
        users[user_id][item_id][action - 1].push(10 / (d * 24 - hour))
    x = []
    y = []
    pairs = []
    c = Counter(len(users), "process training data")
    for user_id in users:
        c.count_print()
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
    filename = "cache/buy_each_day.pickle"
    try:
        buy = load(filename)
        print("load data buy %d %d" % (len(buy), len(buy[0])))
    except FileNotFoundError:
        buy = init_buy_data()
        save(buy, filename)

    return buy


def get_train_data(d, buy):
    x_name = "cache/x_%d.pickle" % d
    y_name = "cache/y_%d.pickle" % d
    p_name = "cache/p_%d.pickle" % d
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
    outfile = open("output/out3.csv", "w")
    for r in result:
        outfile.write(r + "\n")
    outfile.close()


# clf = GradientBoostingClassifier(n_estimators=50)
clf = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=0)
# clf = RandomForestRegressor(n_estimators=50, max_depth=5)

buy = get_buy_data()
for d in range(30, 32):
    print("load date for %d" % d)
    x, y, p = get_train_data(d, buy)
    if d <= 30:
        print("train...")
        clf.fit(x, y)
    if d == 31:
        print("predict...")
        y = clf.predict_proba(x)
        # y = clf.predict(x)
        result = []
        for i in range(len(x)):
            if y[i][1] > 0.04:
                result.append(p[i])
        write_result(result)
