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
    country = user[3]
    day = user[6][:10]
    if country == "CN":
        if day not in user_list:
            user_list[day] = {(user_id, email)}
        else:
            user_list[day].add((user_id, email))
file.close()

save(user_list, "editor_dau.pickle")
