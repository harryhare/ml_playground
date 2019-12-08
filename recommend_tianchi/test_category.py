# 尝试使用模型
# 倒数时间
import numpy as np
import csv
from big3 import *
from util import *
from counter import Counter
from data_day_buy import get_buy_data
from data_item_category import get_item_map

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score

np.random.seed(1337)
n = 23291027

datafile = "fresh_comp_offline/user_sorted_filtered.csv"
datafile_origin = "fresh_comp_offline/tianchi_fresh_comp_train_user.csv"


def init_train_data(d, buy, item_map):
    print("train day %d" % d)
    if d == 31:
        file = open(datafile_origin)
        n = 23291027
    else:
        file = open(datafile)
        n = 4594396
    actions = csv.reader(file)
    _ = next(actions)
    user_item = {}
    user_category = {}
    cc = Counter(n, "prepare training data")
    for row in actions:
        cc.count_print()
        user_id = int(row[0])
        item_id = int(row[1])
        action = int(row[2])
        category_id = int(row[4])
        day = get_day(row[5])
        hour = get_hour(row[5])
        if day >= d:
            continue
        t = 10 / (d * 24 - hour)
        if user_id not in user_item:
            user_item[user_id] = {item_id: [Big3(), Big3(), Big3(), Big3()]}
        if item_id not in user_item[user_id]:
            user_item[user_id][item_id] = [Big3(), Big3(), Big3(), Big3()]
        user_item[user_id][item_id][action - 1].push(t)
        if user_id not in user_category:
            user_category[user_id] = {category_id: [Big3(), Big3(), Big3(), Big3()]}
        if category_id not in user_category[user_id]:
            user_category[user_id][category_id] = [Big3(), Big3(), Big3(), Big3()]
        user_category[user_id][category_id][action - 1].push(t)
    x = []
    y = []
    pairs = []
    cc = Counter(len(user_item), "process training data")
    for user_id in user_item:
        cc.count_print()
        for item_id in user_item[user_id]:
            category_id = item_map[item_id]
            item_info = user_item[user_id][item_id]
            category_info = user_category[user_id][category_id]
            xx = []
            xx.extend(item_info[0].get_values())
            xx.extend(item_info[1].get_values())
            xx.extend(item_info[2].get_values())
            xx.extend(item_info[3].get_values())
            xx.extend(category_info[0].get_values())
            xx.extend(category_info[1].get_values())
            xx.extend(category_info[2].get_values())
            xx.extend(category_info[3].get_values())
            user_item_pair = str(user_id) + "," + str(item_id)
            if user_item_pair in buy[d]:
                yy = 1
            else:
                yy = 0
            x.append(xx)
            y.append(yy)
            pairs.append(user_item_pair)

    file.close()
    return x, y, pairs


def get_train_data(d, buy):
    x_name = "cache/x_category_time_inverse_%d.pickle" % d
    y_name = "cache/y_category_time_inverse_%d.pickle" % d
    p_name = "cache/p_category_time_inverse_%d.pickle" % d
    try:
        x = load(x_name)
        y = load(y_name)
        p = load(p_name)
    except FileNotFoundError:
        x, y, p = init_train_data(d, buy, item_map)
        save(x, x_name)
        save(y, y_name)
        save(p, p_name)
    return x, y, p


#clf = GradientBoostingClassifier(n_estimators=50)
clf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=0)
# clf = RandomForestRegressor(n_estimators=50, max_depth=5)

buy = get_buy_data()
item_map = get_item_map()

for d in range(29, 32):
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
            if y[i][1] > 0.25:
                result.append(p[i])
        write_result(result, "output/time_inverse.csv")
