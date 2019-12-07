import pickle


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
