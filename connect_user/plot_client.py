from util import *
import matplotlib.pyplot as plt

client_list = load("client_cn.pickle")

x = []
y = []
pair = []

for k in client_list.keys():
    x.append(k)
    y.append(len(client_list[k]))
    pair.append((x, y))


index = sorted(range(len(y)), key=lambda x: y[x], reverse=True)
xx=[]
yy=[]


for i in range(len(x)):
    xx.append(x[index[i]])
    yy.append(y[index[i]])
    print("%50s:\t\t%s" % (x[index[i]], y[index[i]]))

plt.scatter(xx, yy, color="#ee0000", label="buy")
plt.show()
