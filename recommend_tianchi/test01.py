import pandas as pd
#'user_id', 'item_id', 'behavior_type', 'user_geohash', 'item_category','time'
actions = pd.read_csv("fresh_comp_offline/tianchi_fresh_comp_train_user.csv")
n=len(actions)
print("total:",n)
behavior_type=[0]*5
for a in actions["behavior_type"]:
    behavior_type[a]+=1
print(behavior_type)


result = set()
for i in range(n):
    if actions["item_id"][i]>1e10:
        print("error!!! item_id > 1e10")
    if actions["time"][i]>='2014-12-17' and actions["behavior_type"][i]==3:
        result.add(str(actions["user_id"][i])+","+str(actions["item_id"][i]))
    if i%100000==0:
        print("progress:",i*100/n,"%")
print(result)