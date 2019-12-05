import gevent
import threading

def eat(name):
    print(threading.current_thread().getName())
    print('%s eat 1' % name)
    gevent.sleep(2)
    print(threading.current_thread().getName())
    print('%s eat 2' % name)

def play(name):
    print(threading.current_thread().getName())
    print('%s play 1' % name)
    gevent.sleep(1)
    print(threading.current_thread().getName())
    print('%s play 2' % name)



g1 = gevent.spawn(eat, 'egon')
g2 = gevent.spawn(play, name='egon')
g1.join()
g2.join()
# 或者gevent.joinall([g1,g2])
print('主')