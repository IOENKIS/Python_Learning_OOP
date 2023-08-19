"""class Cat(object):
    breed = 'pers'

    def hello(*args):
        print('Hello world from kitty', args)

    def show_breed(self):
        print('My breed is %s' % self.breed)

    def show_name(self):
        if hasattr(self, 'name'):
            print('My name is %s' % self.name)
        else:
            print('nothing')

    def set_value(self, value, age = 10):
        self.name = value
        self.age = age
"""


# ДЗ
# Задача 1
class Lion(object):
    def roar(self):
        print('Rrrrrrr!')


simba = Lion()
simba.roar()


# Задача 2
class Counter(object):

    def start_from(self, start=0):
        self.start = start

    def increment(instance):
        instance.start += 1

    def display(instance):
        print('Текущее значение счетчика =', instance.start)

    def reset(instance):
        instance.start = 0


# Задача 3
class Point(object):
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other_point):
        if not isinstance(other_point, Point):
            print('Передана не точка')
            exit(0)
        dinstance = float(((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5)
        return dinstance


p1 = Point()
p2 = Point()
p1.set_coordinates(4, 10)
p2.set_coordinates(5, 8)
d = p1.get_distance(p2)
print(d)
