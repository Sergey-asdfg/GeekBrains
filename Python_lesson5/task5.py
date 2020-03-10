# Lesson 4, Task 5

from functools import reduce

with open('digits.txt', 'w') as f:
    digits = f.writelines('23 876 1 45 897654 9 1')

with open('digits.txt') as f:
    digits = f.readline()

def my_f(num1, num2):
    return int(num1) + int(num2)

print(reduce(my_f, digits.split()))
