# Lesson2, Task 2

my_list = [0,0,0,0,0]

for i in range(0,5):
    my_list[i] = input('Пожалйуста, введите целое число: ')

for i in range(0,4,2):
    temp = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = temp

print(my_list)
