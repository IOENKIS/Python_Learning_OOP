# Вычисляемые property
class Square(object):
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.side ** 2
        return self.side ** 2


# ДЗ
# Задание 1
class Rectangle(object):
    def __init__(self, height, width):
        self.h = height
        self.w = width

    @property
    def area(self):
        return self.h * self.w


"""r1 = Rectangle(5, 8)
r2 = Rectangle(9, 10)

print(r1.area)
print(r2.area)"""


# Задание 2
class Date(object):
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @property
    def date(self):
        return f'{self.d:02}/{self.m:02}/{self.y:04}'

    @property
    def usa_date(self):
        return f'{self.d:02}-{self.m:02}-{self.y:04}'


d1 = Date(5, 10, 2001)
d2 = Date(15, 4, 999)

print(d1.date)
print(d1.usa_date)
print(d2.date)
print(d2.usa_date)

