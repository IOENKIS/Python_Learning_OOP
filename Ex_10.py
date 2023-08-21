# Декоратор Property
import hashlib
import os


class BankAccount(object):
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance


# ДЗ
# Теория 1 (атрибуты только для чтения)

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


# Задание 1

class Notebook(object):
    def __init__(self, list_attr):
        self._notes = list_attr

    @property
    def notes_list(self):
        result = ''
        for i, note in enumerate(self._notes):
            result += '%s. %s\n' % ((i + 1), note)
        return result


"""note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
print(note.notes_list)
"""


# Теория 2 (атрибуты для чтения и записи)

class Square(object):
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = float(value)

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.side = value ** 0.5


# Теория 3 (атрибуты только для записи)
class User(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError('Пароль можно только менять, нельзя смотреть')

    @password.setter
    def password(self, new_pswrd):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            'sha256', new_pswrd.encode('utf-8'), salt, 100_000
        )


# Задача 2
class Money(object):
    def __init__(self, dollars, cents):
        self.total_money = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_money // 100

    @property
    def cents(self):
        return self.total_money % 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_money = (value * 100) + self.cents
        else:
            print('Error dollars')

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 100 > value > 0:
            self.total_money = self.dollars * 100 + value
        else:
            print('Error cents')

    def __str__(self):
        return 'Ваше состояние составляет %s долларов %s центов' % (self.dollars, self.cents)

