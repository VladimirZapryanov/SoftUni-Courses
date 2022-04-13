<<<<<<< HEAD
class vowels:
    vowels = set("aeiouyAEIOUY")

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            value = self.text[self.index]
            if value in self.vowels:
                self.index += 1
                return value

            self.index += 1
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

=======
class vowels:
    vowels = set("aeiouyAEIOUY")

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            value = self.text[self.index]
            if value in self.vowels:
                self.index += 1
                return value

            self.index += 1
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
