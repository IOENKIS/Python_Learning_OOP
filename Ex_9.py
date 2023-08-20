# Property. getter-метод и setter-метод

class BankAccount(object):
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)


# ДЗ
class UserMail(object):
    def __init__(self, login, email_index):
        self.login = login
        self.__email = email_index

    def get_email(self):
        return self.__email

    def set_email(self, new_indx):
        if isinstance(new_indx, str) \
                and new_indx.count('@') == 1 \
                and new_indx.count('.') == 1 \
                and new_indx.index('@') < new_indx.index('.'):
            self.__email = new_indx
        else:
            print('ErrorMail: %s' % new_indx)

    email = property(fget=get_email, fset=set_email)


k = UserMail('Belosnezhka', 'prince@wait.you')
print(k.email)
k.email = [1, 2, 3]
k.email = 'prince@still@.wait'
k.email = 'prince@still.wait'
print(k.email)
