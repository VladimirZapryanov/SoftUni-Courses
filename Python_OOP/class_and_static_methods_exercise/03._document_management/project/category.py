<<<<<<< HEAD
class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def edit(self, new_name):
        self.name = new_name

        return self.name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
=======
class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def edit(self, new_name):
        self.name = new_name

        return self.name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
        