# Lesson 5, Task 3

with open('salaries.txt', encoding='utf-8') as f:
    list_salaries = f.readlines()

total_salaries = 0
list_temp = []
for i in range(len(list_salaries)):
    list_temp = list_salaries[i].split()
    if int(list_temp[1]) < 20000:
        print('Сотрудник с зарплатой меньше 20000: ', list_temp[0])
    total_salaries += int(list_temp[1])

print('Средняя зарплата равна: ', int(total_salaries/len(list_salaries)))