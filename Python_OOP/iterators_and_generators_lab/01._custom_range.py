<<<<<<< HEAD
class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end + 1:
            raise StopIteration

        value = self.start
        self.start += 1
        return value


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
=======
class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end + 1:
            raise StopIteration

        value = self.start
        self.start += 1
        return value


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
