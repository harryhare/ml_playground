from util import *
import csv

# User_ID,Email,User_Created_Time,Country,Client_ID,Active_IP,Active_Time
filename = "/Users/unity/connect_user/editor.csv"
file = open(filename)
reader = csv.reader(file)
header = next(reader)

client_list_cn = {}
client_list = {}


for user in reader:
    user_id = user[0]
    email = user[1]
    country = user[3]
    client_id = user[4]
    day = user[6][:10]

    if client_id not in client_list:
        client_list[client_id] = {(user_id, email)}
    else:
        client_list[client_id].add((user_id, email))
    if country == "CN":
        if client_id not in client_list_cn:
            client_list_cn[client_id] = {(user_id, email)}
        else:
            client_list_cn[client_id].add((user_id, email))
file.close()

save(client_list_cn, "client_cn.pickle")
save(client_list, "client.pickle")
