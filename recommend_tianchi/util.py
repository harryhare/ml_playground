def get_day(x):
    return (int(x[5:7]) - 11) * 30 + int(x[8:10]) - 18
def get_hour(x):
    return get_day(x)*24+int(x[11])
