# Метод __init__
class Cat:
    def __init__(self, name, breed='pers', age=1, color='black'):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

        print('hello new object is', name, breed, age, color)


# Дз
# Задача 1
class Laptop(object):
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + ' ' + model


"""laptop1 = Laptop('Asus', '140-bodkins', '32500')
print(laptop1.price)
print(laptop1.laptop_name)

laptop2 = Laptop('HP', '125-TI', '40500')
print(laptop2.price)
print(laptop2.laptop_name)"""


# Задача 2
class SoccerPlayer(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goal = 0
        self.assists = 0

    def score(self, goal=1):
        self.goal += goal

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print('%s %s - голы: %s, передачи: %s' % (self.surname, self.name, self.goal, self.assists))


"""leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics()

kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()"""


# Задача 3

class Zebra(object):
    def __init__(self):
        self.counter = 0

    def which_stripe(self):
        self.counter += 1

        if self.counter % 2 == 0:
            print('Полоска черная')
        else:
            print('Полоска белая')


"""z1 = Zebra()

z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
z2.which_stripe()"""


# Задача 4

class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        print(f'{self.last_name} {self.first_name}')

    def is_asult(self):
        if self.age > 18:
            return True
        else:
            return False


p1 = Person('Jimi', 'Hendrix', 55)
p1.full_name()
print(p1.is_asult())
