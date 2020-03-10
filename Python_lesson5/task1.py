# Lesson 5, Task 1

with open('1.txt', 'w') as f:
    a = True
    while a:
        new_line = input("Введите строку в одну линию для записи в файл: ")
        if new_line != '':
            f.writelines([new_line, '\n'])
        else:
            a = False
