from util import *
import matplotlib.pyplot as plt

editor_dau = load("editor_dau.pickle")
app_dau = load("app_dau.pickle")

x = []
both = []
editor = []
app = []

for i in range(11, 13):
    for j in range(1, 31):
        if i == 11 and j == 31:
            continue
        day = "2019-%02d-%02d" % (i, j)
        if day not in editor_dau:
            continue
        x.append(day)
        in_both = 0
        for pair in editor_dau[day]:
            if pair in app_dau[day]:
                in_both += 1
        both.append(in_both)
        editor.append(len(editor_dau[day]))
        app.append(len(app_dau[day]))

plt.plot(range(len(x)), both, color="#ee0000", label="both")
plt.plot(range(len(x)), app, color="#00ee00", label="app")
plt.plot(range(len(x)), editor, color="#00eeee", label="editor")
plt.legend(bbox_to_anchor=(1, 0.7))
plt.show()
