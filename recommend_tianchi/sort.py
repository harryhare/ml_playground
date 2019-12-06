from util import *
from counter import Counter
import csv

# 'user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category','time'
file = open("fresh_comp_offline/tianchi_fresh_comp_train_user.csv")
reader = csv.reader(file)
header = next(reader)
n = 23291027

l = []
for i in range(31 * 24):
    l.append([])

c = Counter(n, "read")
for row in reader:
    hour = get_hour(row[5])
    l[hour].append(row)
    c.count_print()
file.close()

c = Counter(n,"write")
file = open("fresh_comp_offline/user_sorted.csv", "w")
writer=csv.writer(file, header)
for i in range(31 * 24):
    for row in l[i]:
        writer.writerow(row)
        c.count_print()
file.close()
