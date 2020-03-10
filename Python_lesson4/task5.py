# Lesson 4, Task 5

from functools import reduce

my_list = [el for el in range(100, 1002, 2)]

def my_func_for_reduce(num1,num2):
    return num1*num2

print(reduce(my_func_for_reduce, my_list))
