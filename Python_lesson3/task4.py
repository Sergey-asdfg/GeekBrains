# Lesson3, Task 4

def my_func(arg1, arg2):
    print(arg1**arg2)
    temp = 1
    for i in range(0, -arg2):
        temp = temp/arg1
    print(temp)

my_func(float(input('Введите первое действительное положительное число: ')), int(input('Введите второе число - отрицательное целое: ')))
