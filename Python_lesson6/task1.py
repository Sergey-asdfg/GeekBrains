# Lesson 6, Task 1

from itertools import cycle
import time

class TrafficLight:

    def __init__(self):
        self.__color = 'red'
        self.running()

    def running(self):
        c = 0
        for i in cycle('ryg'):
            c += 1
            if i == 'r':
                self.__color = 'red'
                print(self.__color)
                time.sleep(7)
            elif i == 'y':
                self.__color = 'yellow'
                print(self.__color)
                time.sleep(2)
            else:
                self.__color = 'green'
                print(self.__color)
                time.sleep(5)
            if c > 5:
                break


traffic_light = TrafficLight()



