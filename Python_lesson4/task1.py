# Lesson 4, Task 1

from sys import argv

name_scipt, my_hours, my_rate, my_bonus = argv

print('Моя зарплата будет: ', int(my_hours)*int(my_rate) + int(my_bonus), ' руб.')
