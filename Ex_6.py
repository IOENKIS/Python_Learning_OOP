import math


class Point(object):
    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print('Точка с координатами (%s, %s)' % (self.x, self.y))

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Точка')

        return math.sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)


# ДЗ
# Задание 1

class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def desctiption(self):
        return '%s is %s years old' % (self.name, self.age)

    def speak(self, sound):
        return '%s says %s' % (self.name, sound)


"""jack = Dog('Jack', 4)

print(jack.desctiption())
print(jack.speak('Гав! Гав!'))
print(jack.speak('Мяу! Мяу!'))"""


# Задание 2

class Stack(object):
    def __init__(self):
        self.values = []

    def push(self, item):
        return self.values.append(item)

    def pop(self):
        if not self.values:
            print('Empty Stack')
        else:
            return self.values.pop()

    def peek(self):
        if not self.values:
            print('Empty Stack')
        else:
            return self.values[-1]

    def is_empty(self):
        if not self.values:
            return True
        else:
            return False

    def size(self):
        return len(self.values)


s = Stack()
s.peek()
print(s.is_empty())
s.push('cat')
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(777)
print(s.pop())
print(s.pop())
print(s.size())
