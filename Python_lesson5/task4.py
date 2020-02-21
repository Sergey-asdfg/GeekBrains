# Lesson5, Task 4

with open('1234.txt', encoding='utf-8') as f:
    list_1234 = f.readlines()

list_temp = []
for i in range(len(list_1234)):
    list_temp = list_1234[i].split()
    print(list_temp)
    if list_temp[0] == 'One':
        list_1234[i] = 'Один - 1\n'
    elif list_temp[0]== 'Two':
        list_1234[i] = 'Два - 2\n'
    elif list_temp[0]== 'Three':
        list_1234[i] = 'Три - 3\n'
    elif list_temp[0]== 'Four':
        list_1234[i] = 'Четыре - 4\n'

with open('4321.txt', 'w', encoding='utf-8') as f:
    list_1234 = f.writelines(list_1234)
