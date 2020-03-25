# Lesson3, Task 2

# var1
def my_func(**kwargs):
    print(kwargs)

my_func(name='Ivan', surname='Ivanov', year_of_birth = 2000, city_of_living = 'Moscow', email='i.ivanov@mail.ru', phone = '+79169999999')

# var2
def my_func(name = '', surname='', year_of_birth = None, city_of_living = '', email='', phone = ''):
    print('name = ', name + ',', 'surname = ', surname + ',', 'year_of_birth = ', str(year_of_birth) + ',', 'city_of_living = ', city_of_living + ',', 'email = ', email + ',', 'phone = ', phone)

my_func(name='Ivan', surname='Ivanov', year_of_birth = 2000, city_of_living = 'Moscow', email='i.ivanov@mail.ru', phone = '+79169999999')

