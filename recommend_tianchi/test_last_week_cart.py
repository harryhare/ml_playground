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

cart = []
browse = []
for i in range(32):
    cart.append(set())
    browse.append(set())

c = Counter(n, "read")
for row in actions:
    pair = row[0] + "," + row[1]
    day = get_day(row[5])
    c.count_print()
    if day==31:
        print(row)
    if row[2] == '3':
        cart[day].add(pair)
    if row[2] == '1':
        browse[day].add(pair)

for i in range(32):
    write_result(cart[i], "output/cart%d.csv" % i)


for i in range(32):
    write_result(browse[i], "output/browse%d.csv" % i)



# cart
# 20 1
# 21 4
# 22 0
# 23 2
# 24 4
# 25 5
# 26 9
# 27 6
# 28 4
# 29 18
# 30 69

# browse
# 29 46
# 30 127


# 20 in browse 30 & 29