def func():
    i=0
    while True:
        a = yield i
        print(a)
        i+=1

g=func()
#print(next(g))
print(g.send(None))
print(g.send("test1"))