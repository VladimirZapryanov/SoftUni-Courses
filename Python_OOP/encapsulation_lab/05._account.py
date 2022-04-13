<<<<<<< HEAD
class Account:
    def __init__(self, current_id, balance, pin):
        self.__id = current_id
        self.balance = balance
        self.__pin = pin

    def __validate_pin(self, pin):
        if not pin == self.__pin:
            return "Wrong pin"

        return self.__id

    def get_id(self, pin):
        return self.__validate_pin(pin)

    def change_pin(self, old_pin, new_pin):
        if not old_pin == self.__pin:
            return "Wrong pin"

        self.__pin = new_pin
        return "Pin changed"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
=======
class Account:
    def __init__(self, current_id, balance, pin):
        self.__id = current_id
        self.balance = balance
        self.__pin = pin

    def __validate_pin(self, pin):
        if not pin == self.__pin:
            return "Wrong pin"

        return self.__id

    def get_id(self, pin):
        return self.__validate_pin(pin)

    def change_pin(self, old_pin, new_pin):
        if not old_pin == self.__pin:
            return "Wrong pin"

        self.__pin = new_pin
        return "Pin changed"


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
