# Lesson 6, Task 2


class Road:

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height
        self.mass = 25
        self.total_mass_asfalt()

    def total_mass_asfalt(self):
        print('Общая масса асфальта =', self._length * self._width * self._height * 25)


total_mass_asfalt = Road(5000, 20, 5)