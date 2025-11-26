from soldier import Soldier


class Room:
    def __init__(self, name_room: int, num_soldiers = 8):
        self.name_room = name_room
        self.num_soldiers = num_soldiers
        self.soldiers_list = []

    def add_soldiers(self, soldier: Soldier):
        if len(self.soldiers_list) == self.num_soldiers:
            raise
        self.soldiers_list.append(soldier)

    def is_room_full(self):
        return len(self.soldiers_list) == self.num_soldiers

    def is_room_empty(self):
        return len(self.soldiers_list) == 0

    def is_partial_room(self):
        return not self.is_room_full() and not self.is_room_empty()

