import pickle


def get_cn_day(x):
    return get_day(x)


def get_day(x):
    return (int(x[5:7]) - 11) * 30 + int(x[8:10]) - 18


def get_hour(x):
    return get_day(x) * 24 + int(x[11:])


def save(data, filename):
    ff = open(filename, "wb")
    pickle.dump(data, ff)
    ff.close()


def load(filename):
    ff = open(filename, "rb")
    data = pickle.load(ff)
    ff.close()
    return data


def write_result(result, file_name="output/out.csv"):
    print("write result")
    outfile = open(file_name, "w")
    outfile.write("user_id,item_id\n")
    for r in result:
        outfile.write(r + "\n")
    outfile.close()


def get_match_count(f1, c):
    y = 517
    return f1 * (c + y) / 2


def need_right_result(c):
    return get_match_count(0.1, c)






def sort_map(m):
    x = []
    y = []
    pair = []

    for k in m.keys():
        x.append(k)
        y.append(m[k])
        pair.append((x, y))

    index = sorted(range(len(y)), key=lambda x: y[x], reverse=True)
    xx = []
    yy = []

    for i in range(len(x)):
        xx.append(x[index[i]])
        yy.append(y[index[i]])
        print("%50s:\t\t%s" % (x[index[i]], y[index[i]]))
    return xx, yy
