#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import utils.ioutil as ioutil
import threading
from threading import Thread, Condition
import time
import random

current = 'A'
condition = Condition()

class threadA(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self) -> None:
        global current
        for _ in range(10):
            if 'A' == current:
                print('here goes A')
                current = 'B'
                condition.notify_all()
                condition.release()
            condition.wait()

class threadB(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self) -> None:
        global current
        for _ in range(10):
            if 'B' == current:
                print('here goes B')
                current = 'C'
                condition.notify_all()
                condition.release()
            condition.wait()

class threadC(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self) -> None:
        global current
        for _ in range(10):
            if 'C' == current:
                print('here goes C')
                current = 'A'
                condition.notify_all()
                condition.release()
            condition.wait()

if __name__ == '__main__':
    threadA = threadA()
    threadB = threadB()
    threadC = threadC()

    threadA.start()
    threadB.start()
    threadC.start()
    threadA.join()
    threadB.join()
    threadC.join()

