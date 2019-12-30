from util import *
import csv

# EventType,AppVersion,GenesisId,Email,UserId,FullName,Device,AppTime,CreatedTime,System,UserAgent,DeletedTime,DeletedReason,DeletedBy,enableNotification,subtype,id,type,duration,index,state,success,articleId,favoriteId
filename = "/Users/unity/connect_user/app.12.csv"
file = open(filename)
reader = csv.reader(file)
header = next(reader)

user_list = {}

for user in reader:
    user_id = user[2]
    email = user[3]
    day = user[8][:10]
    if day not in user_list:
        user_list[day] = {(user_id, email)}
    else:
        user_list[day].add((user_id, email))
file.close()

filename = "/Users/unity/connect_user/app.11.csv"
file = open(filename)
reader = csv.reader(file)
header = next(reader)

for user in reader:
    user_id = user[2]
    email = user[3]
    day = user[8][:10]
    if day not in user_list:
        user_list[day] = {(user_id, email)}
    else:
        user_list[day].add((user_id, email))
file.close()

save(user_list, "app_dau.pickle")
