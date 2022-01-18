from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def _get_room_by_number(self, room_number):
        possible_rooms = [r for r in self.rooms if r.number == room_number]
        return possible_rooms[0]

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self._get_room_by_number(room_number)
        if room.take_room(people):
            return

        self.guests += people

    def free_room(self, room_number):
        room = self._get_room_by_number(room_number)
        self.guests -= room.guests
        if room.free_room():
            return

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests" + "\n"
        result += f"Free rooms: {', '.join(str(x.number) for x in self.rooms if not x.is_taken)}" + "\n"
        result += f"Taken rooms: {', '.join(str(x.number) for x in self.rooms if x.is_taken)}"

        return result

