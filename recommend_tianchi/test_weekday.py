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
bought_exclude_12_12 = set()
bought_sample=set()

c = Counter(n, "read")
for row in actions:
    pair = row[0] + "," + row[1]
    day = get_day(row[5])
    c.count_print()
    if row[2] == "4":
        if day % 7 == 3 and day != 24:
            bought_exclude_12_12.add(pair)
        if day % 7 == 3:
            bought.add(pair)
        if day==17:
            bought_sample.add(pair)

print(len(bought))
print(len(bought_exclude_12_12))
print(len(bought_sample))
write_result(bought, "output/same_weekday.csv")  #4 # 0.00018
write_result(bought_exclude_12_12, "output/same_weekday_exclude_12_12.csv") #2 # 0.00024
write_result(bought_sample,"output/bought_sample.csv") #1
