# Lesson3, Task 4

my_list = [10,90,90,20,20,30,40,60,40,50,60,70,80,80]

def generator():
    my_list_ = []
    my_set = set(my_list)
    for el in my_list:
        if el in my_set:
            my_set.discard(el)
        else:
            my_list_.append(el)
    yield my_list_

g = generator()
for i in g:
    print(i)

