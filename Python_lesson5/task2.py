# Lesson 5, Task 2

with open('1.txt') as f:
    my_list_lines = f.readlines()

print('Количество строк в файле:', len(my_list_lines))

print('Количество символов в каждой строке:')
for i in range(len(my_list_lines)):
    print(len(my_list_lines[i]) - 1)