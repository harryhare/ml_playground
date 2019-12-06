import pickle

def save(data, filename):
    ff = open(filename, "wb")
    pickle.dump(data, ff)
    ff.close()


def load(filename):
    ff = open(filename, "rb")
    data = pickle.load(ff)
    ff.close()
    return data

def get_day(x):
    return (int(x[5:7]) - 11) * 30 + int(x[8:10]) - 18


def get_hour(x):
    return get_day(x) * 24 + int(x[11])

buy=load("buy_each_day.pickle")