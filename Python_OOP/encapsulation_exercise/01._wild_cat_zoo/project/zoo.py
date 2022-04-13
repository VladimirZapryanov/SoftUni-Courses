<<<<<<< HEAD
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity <= 0:
            return f"Not enough space for animal"

        if price > self.__budget:
            return f"Not enough budget"

        self.animals.append(animal)
        self.__animal_capacity -= 1
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= 0:
            return "Not enough space for worker"

        self.workers.append(worker)
        self.__workers_capacity -= 1
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary

        if total_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care

        if total_money_for_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals" + "\n"

        result += self.__get_animals_status_by_type("Lion")
        result += self.__get_animals_status_by_type("Tiger")
        result += self.__get_animals_status_by_type("Cheetah")

        return result.strip()

    def __get_animals_status_by_type(self, animal_type):
        animals = [str(x) for x in self.animals if x.__class__.__name__ == animal_type]

        result = f"----- {len(animals)} {animal_type}s:" + "\n"

        for animal in animals:
            result += animal
            result += "\n"

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers" + "\n"

        result += self.__get_workers_status_by_type("Keeper")
        result += self.__get_workers_status_by_type("Caretaker")
        result += self.__get_workers_status_by_type("Vet")

        return result.strip()

    def __get_workers_status_by_type(self, worker_type):
        workers = [str(x) for x in self.workers if x.__class__.__name__ == worker_type]

        result = f"----- {len(workers)} {worker_type}s:" + "\n"

        for worker in workers:
            result += worker
            result += "\n"

        return result

=======
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity <= 0:
            return f"Not enough space for animal"

        if price > self.__budget:
            return f"Not enough budget"

        self.animals.append(animal)
        self.__animal_capacity -= 1
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= 0:
            return "Not enough space for worker"

        self.workers.append(worker)
        self.__workers_capacity -= 1
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary

        if total_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care

        if total_money_for_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals" + "\n"

        result += self.__get_animals_status_by_type("Lion")
        result += self.__get_animals_status_by_type("Tiger")
        result += self.__get_animals_status_by_type("Cheetah")

        return result.strip()

    def __get_animals_status_by_type(self, animal_type):
        animals = [str(x) for x in self.animals if x.__class__.__name__ == animal_type]

        result = f"----- {len(animals)} {animal_type}s:" + "\n"

        for animal in animals:
            result += animal
            result += "\n"

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers" + "\n"

        result += self.__get_workers_status_by_type("Keeper")
        result += self.__get_workers_status_by_type("Caretaker")
        result += self.__get_workers_status_by_type("Vet")

        return result.strip()

    def __get_workers_status_by_type(self, worker_type):
        workers = [str(x) for x in self.workers if x.__class__.__name__ == worker_type]

        result = f"----- {len(workers)} {worker_type}s:" + "\n"

        for worker in workers:
            result += worker
            result += "\n"

        return result

>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
