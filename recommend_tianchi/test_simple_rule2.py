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
    if '2014-12-11 00' <= row[5] < "2014-12-12":
        if row[2] == "3":
            predict.add(row[0] + "," + row[1])
        elif row[2] == "4":
            bought.add(row[0] + "," + row[1])

    if '2014-12-12' <= row[5] < "2014-12-13":
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

# 50260039,251443481
# 11594934,55559718
# 134116374,167063158
# 134116374,242125236
# 18959614,61535141
# 11366706,233101284
# 18959614,108852248
# 132236660,180933374
# 11594934,144053049
# 57460275,331212270
# 18488008,268865942
# 112141018,31193281
# 18488008,163689973
# 135378246,21875449
# 56818905,192196843
# 42793246,77414788
# 42793246,125634399
# 117707223,344609145
# 128441868,276316706
# 136286592,159396014
# 103823974,37910916
# 4498439,74977824
# 18959614,89867174
# 18959614,46655123
# 112141018,186834589
# 22726524,272369633
# 42096946,23893034
# 8883723,260226898
# 12952941,316324532
