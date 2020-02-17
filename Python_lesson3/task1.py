# Lesson3, Task 1

my_list = [0,0]
for i in range(0,2):
    my_list[i] = int(input('Введите ' + str(i+1) + '-е целое число: '))

try:
   print(my_list[0]/my_list[1])
except ZeroDivisionError:
   print('Деление на ноль (второе число ноль)')
