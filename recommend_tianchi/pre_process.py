import csv
from counter import Counter

# 'user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category','time'
file = open("fresh_comp_offline/user_sorted.csv")
reader = csv.reader(file)
header = next(reader)
n = 23291027

buy_direct = 0
users = set()
items = set()
categories = set()

c = Counter(n, "read")
for row in reader:
    c.count_print()
    user_id = row[0]
    item_id = row[1]
    action = row[2]
    category_id = row[4]
    if action == "4":
        users.add(user_id)
        items.add(item_id)
        categories.add(category_id)
file.close()

print("user in use:", len(users))
print("item in use:", len(items))
print("category in user:", len(categories))

# user in use: 17654

# item in use: 170451
# category in user: 5581

file_in = open("fresh_comp_offline/user_sorted.csv", "r")
file_out = open("fresh_comp_offline/user_sorted_filtered.csv", "w")
reader = csv.reader(file_in)
writer = csv.writer(file_out)
writer.writerow(next(reader))
c = Counter(n, "filter")
valid_row = 0
for row in reader:
    c.count_print()
    user_id = row[0]
    item_id = row[1]
    category_id = row[4]
    if user_id not in users:
        continue
    if item_id not in items:
        continue
    if category_id not in categories:
        continue
    writer.writerow(row)
    valid_row += 1
file_in.close()
file_out.close()
print("valid row: ", valid_row)  # 4594396
