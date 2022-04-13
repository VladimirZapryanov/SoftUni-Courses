<<<<<<< HEAD
class Trainer:
    id = 1

    def __init__(self, name):
        self.id = Trainer.get_next_id()
        self.name = name

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        res = Trainer.id
        Trainer.id += 1
=======
class Trainer:
    id = 1

    def __init__(self, name):
        self.id = Trainer.get_next_id()
        self.name = name

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        res = Trainer.id
        Trainer.id += 1
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
        return res