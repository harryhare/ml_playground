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
predict = set()
bought = set()
real = set()
for row in actions:
    if row[5] >= '2014-12-11 00' and row[5] < "2014-12-12":
        if row[2] == "3":
            predict.add(row[0] + "," + row[1])
        elif row[2] == "4":
            bought.add(row[0] + "," + row[1])

    if row[5] >= '2014-12-12' and row[5] < "2014-12-13":
        if row[2] == "4":
            real.add(row[0] + "," + row[1])
    i += 1
    if i % 100000 == 0:
        print("progress:", i * 100 / n, "%")

for b in bought:
    if b in predict:
        predict.remove(b)
print("predict:", len(predict))
print("real:", len(real))
match = 0
for p in predict:
    if p in real:
        match += 1
print("match:", match)
print("precision:", match / len(predict))
print("recall:", match / len(real))
print("f1:", 2 * match / (len(predict) + len(real)))
