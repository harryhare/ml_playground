
def foo():
    print("starting...")
    # while True:
    #     res = yield 4
    #     print("res:",res)
    while True:
        for i in range(4):
            yield i

g=foo()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
