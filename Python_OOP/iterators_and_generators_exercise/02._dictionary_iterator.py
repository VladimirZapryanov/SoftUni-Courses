<<<<<<< HEAD
class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.keys_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.keys_index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.keys_index]
        value = self.dictionary[key]
        self.keys_index += 1
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

=======
class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.keys_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.keys_index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.keys_index]
        value = self.dictionary[key]
        self.keys_index += 1
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
