from threading import Thread
from time import sleep


class A(Thread):
    def run(self):
        for i in range(10):
            print(i)
            sleep(0.5)

class B(Thread):
    def run(self):
        for i in range(10):
            print(i)
            sleep(0.5)

t1 = A()
t2 = B()


t1.start()
t2.start()