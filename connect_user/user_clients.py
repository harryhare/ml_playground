from util import *
import csv

# User_ID,Email,User_Created_Time,Country,Client_ID,Active_IP,Active_Time
filename = "/Users/unity/connect_user/editor.csv"
file = open(filename)
reader = csv.reader(file)
header = next(reader)

user_clients = {}

for user in reader:
    user_id = user[0]
    email = user[1]
    country = user[3]
    client_id = user[4]
    day = user[6][:10]
    if user_id not in user_clients:
        user_clients[user_id] = {client_id}
    else:
        user_clients[user_id].add(client_id)
file.close()

save(user_clients, "user_clients.pickle")
