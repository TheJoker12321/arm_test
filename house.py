from room import Room


class House:
    def __init__(self,name_house, num_rooms = 10):
        self.name_house = name_house
        self.num_rooms = num_rooms
        self.rooms_list = []

    def add_room(self, room: Room):
        if len(self.rooms_list) == self.num_rooms:
            raise
        self.rooms_list.append(room)

