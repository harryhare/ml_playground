# 最后几小时加入购物后而没有购买的物品
import csv
from util import *
from counter import Counter

# 'user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category','time'
file = open("fresh_comp_offline/tianchi_fresh_comp_train_user.csv")
actions = csv.reader(file)
header = next(actions)
n = 23291027

result = set()
bought = set()
c = Counter(n, "read")
for row in actions:
    c.count_print()
    if row[5] >= '2014-12-18 21':
        if row[2] == "3":
            result.add(row[0] + "," + row[1])
        elif row[2] == "4":
            bought.add(row[0] + "," + row[1])

print(len(result))
print(len(bought))
write_result(result, "output/simple.csv")  # 0.01643
# (4474+539)*0.01643 =41
for b in bought:
    if b in result:
        result.remove(b)
write_result(result, "output/simple_without_bought.csv")  # 0.01825
# (3867+539)*0.01825/2=40
