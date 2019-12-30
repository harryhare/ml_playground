from util import *
import matplotlib.pyplot as plt

dau = load("editor_dau.pickle")

x = []
y = []


for i in range(11, 13):
    for j in range(1, 31):
        if i == 11 and j == 31:
            continue
        day = "2019-%02d-%02d" % (i, j)
        if day not in dau:
            continue
        x.append(day)
        y.append(len(dau[day]))

plt.plot(range(len(x)), y, color="#ee0000", label="buy")
plt.show()
