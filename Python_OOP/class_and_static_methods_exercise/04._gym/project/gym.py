from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.__get_obj_by_id(self.subscriptions, subscription_id)
        customer = self.__get_obj_by_id(self.customers, subscription_id)
        trainer = self.__get_obj_by_id(self.trainers, subscription_id)
        equipment = self.__get_obj_by_id(self.equipment, subscription_id)
        plan = self.__get_obj_by_id(self.plans, subscription_id)

        result = f"{str(subscription)}" + "\n" + f"{str(customer)}" + "\n" + f"{str(trainer)}" + "\n" + f"{str(equipment)}" + "\n" + f"{str(plan)}"
        return result

    def __get_obj_by_id(self, objects, id):
        for object in objects:
            if object.id == id:
                return object

