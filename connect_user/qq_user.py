from util import *
import csv

# EventType,AppVersion,GenesisId,Email,UserId,FullName,Device,AppTime,CreatedTime,System,UserAgent,DeletedTime,DeletedReason,DeletedBy,enableNotification,subtype,id,type,duration,index,state,success,articleId,favoriteId
filename = "/Users/unity/connect_user/app.12.csv"
file = open(filename)
reader = csv.reader(file)
header = next(reader)

user_list = set()

for user in reader:
    user_id = user[2]
    email = user[3]
    user_list.add((user_id, email))
file.close()

filename = "/Users/unity/connect_user/app.11.csv"
file = open(filename)
reader = csv.reader(file)
header = next(reader)

for user in reader:
    user_id = user[2]
    email = user[3]
    user_list.add((user_id, email))
file.close()

save(user_list, "users.pickle")
