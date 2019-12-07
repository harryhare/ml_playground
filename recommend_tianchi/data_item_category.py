from util import *
import csv
from counter import Counter

item_file = "fresh_comp_offline/tianchi_fresh_comp_train_item.csv"
user_file = "fresh_comp_offline/tianchi_fresh_comp_train_user.csv"
n = 23291027


def init_item_map():
    with open(item_file, "r") as file:
        reader = csv.reader(file)
        next(reader)
        m = {}
        for row in reader:
            item_id = int(row[0])
            category_id = int(row[2])
            m[item_id] = category_id
    return m


def init_item_map2():
    with open(user_file, "r") as file:
        reader = csv.reader(file)
        next(reader)
        m = {}
        c = Counter(n,"read")
        for row in reader:
            c.count_print()
            item_id = int(row[1])
            category_id = int(row[4])
            m[item_id] = category_id
    return m


def get_item_map():
    filename = "cache/item_category.pickle"
    try:
        m = load(filename)
    except FileNotFoundError:
        m = init_item_map2()
        save(m, filename)
    return m


if __name__ == "__main__":
    m = get_item_map()
