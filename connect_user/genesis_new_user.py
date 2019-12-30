from util import *
import csv

# User_ID,Email,User_Created_Time,Country,Client_ID,Active_IP,Active_Time
filename = "/Users/unity/connect_user/editor.csv"
file = open(filename)
reader = csv.reader(file)
header = next(reader)

user_list = {}

for user in reader:
    user_id = user[0]
    email = user[1]
    create_time = user[2][:10]
    country = user[3]
    day = user[6][:10]
    if country == "CN":
        if create_time not in user_list:
            user_list[create_time] = {(user_id, email)}
        else:
            user_list[create_time].add((user_id, email))
file.close()

save(user_list, "create_user_cn.pickle")
