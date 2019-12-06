import csv
import matplotlib.pyplot as plt

# 'user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category','time'
file = open("fresh_comp_offline/tianchi_fresh_comp_train_user.csv")
actions = csv.reader(file)
header = next(actions)
n = 23291027

i = 0

items = {}
users = {}
categories = set()
date_buy = [0] * 32
date_cart = [0] * 32
date_mark = [0] * 32
date_browse = [0] * 32
begin_day = "2014-11-18"


def get_day(x):
    return (int(x[5:7]) - 11) * 30 + int(x[8:10]) - 18


for row in actions:
    user_id = row[0]
    item_id = row[1]
    action = row[2]
    c = row[4]
    d = row[5][0:10]
    day = get_day(d)
    if action == "4":
        if user_id in users:
            users[user_id].add(item_id)
        else:
            users[user_id] = {item_id}
        if item_id in items:
            items[item_id].add(user_id)
        else:
            items[item_id] = {user_id}
        categories.add(c)
    if action == "4":
        date_buy[day] += 1
    if action == "3":
        date_cart[day] += 1
    if action == "2":
        date_mark[day] += 1
    if action == "1":
        date_browse[day] += 1
    i += 1
    if i % 200000 == 0:
        print("progress:\t%0.2f%%" % (i * 100 / n))

for i in range(30):
    date_browse[i] = date_browse[i] / 20

plt.plot(range(30), date_buy[:30], color="#ee0000", label="buy")
plt.plot(range(30), date_cart[:30], color="#eeee00", label="cart")
plt.plot(range(30), date_mark[:30], color="#00eeee", label="mark")
plt.plot(range(30), date_browse[:30], color="#0000ee", label="browse")
plt.legend(bbox_to_anchor=(1, 0.7))
plt.show()

print("users: ", len(users))
print("items: ", len(items))
print("categories: ", len(categories))
