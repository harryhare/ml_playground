# 收藏过，加入购物车过，购买过
# 不考虑时间顺序

import csv
from util import *
from counter import Counter

# 'user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category','time'
file = open("fresh_comp_offline/user_sorted.csv")
actions = csv.reader(file)
header = next(actions)
n = 23291027

bought = set()
bought_twice = set()
bought_third = set()

c = Counter(n, "read")
for row in actions:
    pair = row[0] + "," + row[1]
    c.count_print()
    if row[2] == '4':
        if pair in bought_twice:
            bought_third.add(pair)
        if pair in bought:
            bought_twice.add(pair)
        else:
            bought.add(pair)

write_result(bought_twice, "output/buy_twice.csv")  # 6 # 0.00057 # 20573
write_result(bought_third, "output/buy_third.csv")  # 3 # 0.00096 # 5748
