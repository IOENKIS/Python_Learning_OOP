# Public, protected, private attr and methods

class BankAccount(object):
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_data(self):
        self.__print_private_data()

    """def print_protected_data(self):
        print(self._name, self._balance, self._passport)"""

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


"""account1 = BankAccount('Bob', 100000, 243242_1324)
print(account1._BankAccount__balance)
print(dir(account1))"""
"""print(account1.__name)
print(account1.__balance)
print(account1.__passport)"""


# ДЗ
# Задание 1

class Student(object):
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display(self):
        print('Имя: %s\nВозраст: %s\nНаправление: %s' % (self.__name, self.__age, self.__branch))

    def access_private_method(self):
        self.__display()


"""obj = Student('Adam Smith', 25, 'Information Technology')
obj.access_private_method()"""


# Задание 2
class PizzaMaker(object):
    def __make_pepperoni(self):
        print('Пицца Пепперони')

    def _make_barbecue(self):
        print('BBQ')


customer1 = PizzaMaker()
customer1._make_barbecue()
customer1._PizzaMaker__make_pepperoni()
