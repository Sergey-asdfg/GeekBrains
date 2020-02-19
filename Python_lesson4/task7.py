# Lesson 4, Task 7
import math

def fibo_gen():
    factorial_list = [math.factorial(el) for el in range(15)]
    yield factorial_list

print([el for el in fibo_gen()])