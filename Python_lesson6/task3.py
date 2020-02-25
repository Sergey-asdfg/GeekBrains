# Lesson 6, Task 3

class Worker:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.position = 'worker'
        self._income = {'name': name, 'surname': surname, 'wage': 100, 'bonus': 50}

class Position(Worker):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.get_full_name()
        self.get_total_income()

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def  get_total_income(self):
        total_income = (int(self._income['wage'] + int(self._income['bonus'])))
        print(total_income)


to_get_income = Position('Ivan', 'Ivanov')

