# Lesson 5, Task 6

with open('training_plan.txt', encoding='utf-8') as f:
    list_training_plan = f.readlines()

d = {}
list_temp = []
for i in range(len(list_training_plan)):
    list_temp = list_training_plan[i].split()
    d[list_temp[0]] = int(list_temp[1]) + int(list_temp[2]) + int(list_temp[3])
    
print(d) # выводит в рандомном порядке
