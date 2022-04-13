<<<<<<< HEAD
class Stack(list):
    def __init__(self):
        super().__init__()
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        last_element = self.data.pop()
        return last_element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(self.data[::-1])}]"



=======
class Stack(list):
    def __init__(self):
        super().__init__()
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        last_element = self.data.pop()
        return last_element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(self.data[::-1])}]"



>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
