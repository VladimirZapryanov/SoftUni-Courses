<<<<<<< HEAD
class Topic:
    def __init__(self, id, topic, storage_folder):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic, new_storage_folder):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

        return self.topic, self.storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
=======
class Topic:
    def __init__(self, id, topic, storage_folder):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic, new_storage_folder):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

        return self.topic, self.storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
