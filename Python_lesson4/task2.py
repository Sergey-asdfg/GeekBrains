# Lesson 4, Task 2

my_list = [1,2,3,2,4,5,5,4,6,7]

def generator():
    for i in range(len(my_list)-1):
        if my_list[i+1] > my_list[i]:
            yield my_list[i+1]
g = generator()
for i in g:
    print(i)
