# 最后几小时加入购物后而没有购买的物品
import csv

# 'user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category','time'
file = open("fresh_comp_offline/tianchi_fresh_comp_train_user.csv")
actions = csv.reader(file)
header = next(actions)
n = 23291027

i = 0
# for row in actions:
#     print(row)
#     i+=1
#     if(i>100):
#         break
result = set()
bought = set()
for row in actions:
    if row[5] >= '2014-12-18 00':
        if row[2] == "3":
            result.add(row[0] + "," + row[1])
        elif row[2] == "4":
            bought.add(row[0] + "," + row[1])
    i += 1
    if i % 100000 == 0:
        print("progress:", i * 100 / n, "%")
print(len(result))
print(len(bought))
for b in bought:
    if b in result:
        result.remove(b)
out = open("output/out2.csv", "w")
out.write("user_id,item_id\n")
for r in result:
    out.write(r + "\n")
out.close()
