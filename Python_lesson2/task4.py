# Lesson2, Task 4

stroke = input('Введите строку: ')

stroke_split = stroke.split()
number_words = len(stroke_split)

for i in range (0, number_words):
    if len(stroke_split[i]) <= 10:
        print(str(i + 1)+ ' ' + stroke_split[i])
    else:
        print(str(i + 1) + ' ' + stroke_split[i][:10])