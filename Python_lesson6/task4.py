# Lesson6, Task 4

class Car:

    def __init__(self, speed, name, color, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print('turn to', direction)

    def show_speed(self):
        print('You are:', self.name)
        print('Your speed:', self.speed)

class TownCar(Car):

    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)
        self.show_speed()

    def show_speed(self):
        print('You are:', self.name)
        if self.speed > 60:
            print('Your speed is over 60km/h')
        else:
            print('Your speed:', self.speed)

class SportCar(Car):

    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)
        self.show_speed()

class WorkCar(Car):

    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)
        self.show_speed()

    def show_speed(self):
        print('You are:', self.name)
        if self.speed > 40:
            print('Your speed is over 40km/h')
        else:
            print('Your speed:', self.speed)

class PoliceCar(Car):

    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)
        self.show_speed()


town_car = TownCar(80, 'Toyota', 'Red', False)
work_car = WorkCar(60, 'Caterpiller', 'Yellow', False)
sport_car = SportCar(120, 'Porshe', 'Red', False)
police_car = PoliceCar(120, 'Crysler', 'White', True)
