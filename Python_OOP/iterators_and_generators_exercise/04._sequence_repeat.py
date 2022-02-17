class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration

        ch = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        self.number -= 1

        return ch


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')




