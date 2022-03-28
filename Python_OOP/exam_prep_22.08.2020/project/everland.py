from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumptions = 0
        for room in self.rooms:
            total_consumptions += room.expenses + room.room_cost

        return f"Monthly consumptions: {total_consumptions:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost
            if total_cost > room.budget:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

            room.budget -= total_cost
            result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")

        return "\n".join(result)

    def status(self):
        result = ""
        result += f"Total population: {sum([r.members_count for r in self.rooms])}\n"

        for r in self.rooms:
            result += f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n"

            if r.children:
                count = 0
                for ch in r.children:
                    count += 1
                    result += f"--- Child {count} monthly cost: {ch.get_monthly_expense():.2f}$\n"

            if hasattr(r, 'appliances'):
                total_expenses = 0
                for a in r.appliances:
                    total_expenses += a.get_monthly_expense()
                result += f"--- Appliances monthly cost: {total_expenses:.2f}$\n"

        return result





