import threading


def t1(cond):
    with cond:
        for i in range(100):
            if i % 2 == 0:
                print(i)
            cond.notify()
            cond.wait()


def t2(cond):
    with cond:
        for i in range(100):
            cond.wait()
            if i % 2 != 0:
                print(i)
            cond.notify()


if __name__ == '__main__':
    cond = threading.Condition()
    thread1 = threading.Thread(target=t1, args=(cond,))
    thread2 = threading.Thread(target=t2, args=(cond,))
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()
