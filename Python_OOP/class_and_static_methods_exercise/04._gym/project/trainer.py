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
        return res