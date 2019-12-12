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
cart = set()
mark = set()
all3 = set()

bought_cart = set()
bought_mark = set()
cart_mark = set()

c = Counter(n, "read")
for row in actions:
    pair = row[0] + "," + row[1]
    c.count_print()
    if row[2] == "3":
        all3.add(pair)
        cart.add(pair)
        bought_cart.add(pair)
        cart_mark.add(pair)
    elif row[2] == "4":
        all3.add(pair)
        bought.add(pair)
        bought_mark.add(pair)
        bought_cart.add(pair)
    elif row[2] == "2":
        all3.add(pair)
        mark.add(pair)
        bought_mark.add(pair)
        cart_mark.add(pair)

write_result(all3, "output/all3.csv")  # 162 # 0.00032 #162
write_result(cart, "output/cart.csv")  # 122 # 0.00045/10 # 122
write_result(mark, "output/mark.csv")  # 30 # 0.00014/8
write_result(bought, "output/bought.csv") #29  # 0.00029/3.6
write_result(bought_cart, "output/bought_cart.csv") #138   # 0.00044/11
write_result(bought_mark, "output/bought_mark.csv") #54 #0.00018
write_result(cart_mark, "output/cart_mark.csv") #150 #0.00032

bought_and_cart = set()
for x in bought:
    if x in cart:
        bought_and_cart.add(x)

cart_not_buy_yet = set()
for x in cart:
    if x not in bought:
        cart_not_buy_yet.add(x)


write_result(bought_and_cart, "output/bought_and_cart.csv")  # 15 # 0.00026/2.1
write_result(cart_not_buy_yet, "output/cart_not_buy_yet.csv") # 109 # 0.00051
