from util import *
import matplotlib.pyplot as plt

user_list = load("create_user_cn.pickle")

m = {}
for x in user_list.keys():
    m[x] = len(user_list[x])

xx, yy = sort_map(m)

plt.scatter(xx, yy)
plt.show()
