# Lesson 4, Task 6

from itertools import cycle, count

for el in count(10):
    print(el)
    if el > 19:
        break

c=0
for el in cycle('abcdefgh'):
    c += 1
    print(el)
    if c > 30:
        break