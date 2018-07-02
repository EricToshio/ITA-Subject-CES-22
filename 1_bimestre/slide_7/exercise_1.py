'''
Exercício:
Implemente o problema do produtor consumidor usando Rlock ao invés de uma fila.
'''

from queue import Queue
from threading import Thread, RLock
import time
import random

number_of_items = 10

class Box(object):
    lock = RLock()
    def __init__(self, number):
        self.total_items = number
        self.items = []
    def add(self, item):
        Box.lock.acquire()
        self.items.append(item)
        Box.lock.release()
    def get(self):
        Box.lock.acquire()
        try:
            first = self.items[0]
        except:
            first = None
        Box.lock.release()
        return first
    def remove(self, item):
        Box.lock.acquire()

        removed = False
        try:
            self.items.remove(item)
            self.total_items -= 1
            removed = True
        except:
            pass


        Box.lock.release()
        return removed

class producer(Thread):
    def __init__(self, box):
        Thread.__init__(self)
        self.box = box

    def run(self):
        for i in range(number_of_items):
            item = random.randint(0, 256)
            box.add(item)
            print('Producer notify: item Nº %d add to Box by %s \n' % (item, self.name))
            time.sleep(1)

class consumer(Thread):
    def __init__(self, box):
        Thread.__init__(self)
        self.box = box

    def run(self):
        while box.total_items > 0 :
            item = box.get()
            if item != None:
                if box.remove(item):
                    print('Consumer notify: %d removed from the Box by %s \n' % (item, self.name))


if __name__ == "__main__":
    box = Box(number_of_items)
    t1 = producer(box)
    t2 = consumer(box)
    t3 = consumer(box)
    t4 = consumer(box)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("finished to sell %d items!!!\n" % number_of_items)