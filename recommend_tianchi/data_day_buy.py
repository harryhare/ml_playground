import csv
from counter import Counter
from util import *

n = 23291027

datafile = "fresh_comp_offline/user_sorted_filtered.csv"
datafile_origin = "fresh_comp_offline/tianchi_fresh_comp_train_user.csv"


def init_buy_data():
    file = open(datafile)
    actions = csv.reader(file)
    _ = next(actions)
    buy = []
    for j in range(32):
        buy.append(set())
    cc = Counter(n, "calculate bought items")
    for row in actions:
        cc.count_print()
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


def get_buy_data():
    filename = "cache/buy_each_day.pickle"
    try:
        buy = load(filename)
    except FileNotFoundError:
        buy = init_buy_data()
        save(buy, filename)
    return buy


if __name__ == "__main__":
    buy = get_buy_data()
