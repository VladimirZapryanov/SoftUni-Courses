<<<<<<< HEAD
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account, amount_to_add):
        new_balance = account.balance + amount_to_add
        if new_balance < 0:
            raise ValueError("sorry cannot go in debt!")

        account.add_transaction(amount_to_add)
        return f"New balance: {new_balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new_acc = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)

        for tx in self._transactions:
            new_acc.add_transaction(tx)

        for tx in other._transactions:
            new_acc.add_transaction(tx)

        return new_acc


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

=======
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        self._transactions.append(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def validate_transaction(account, amount_to_add):
        new_balance = account.balance + amount_to_add
        if new_balance < 0:
            raise ValueError("sorry cannot go in debt!")

        account.add_transaction(amount_to_add)
        return f"New balance: {new_balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new_acc = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)

        for tx in self._transactions:
            new_acc.add_transaction(tx)

        for tx in other._transactions:
            new_acc.add_transaction(tx)

        return new_acc


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
