from threading import Thread

a = 0

def f():
    global a
    for i in range(200000):
        a += 1

def test():
    global a
    a = 0

    t = Thread(target=f)
    s = Thread(target=f)

    t.start()
    s.start()

    t.join()
    s.join()

for i in range(1, 5):
    test()
    print("in test {}: value of a is {} but must be {}".format(i, a, 200000*2))