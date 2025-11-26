from logic_army.house import House


class Basis:
    def __init__(self, houses = 2, name = "Shivat hashibolim"):
        self.houses = houses
        self.name = name
        self.houses_list = []
        self.soldiers_without_house = []

    def add_house(self, house: House):
        if len(self.houses_list) == self.houses:
            raise
        self.houses_list.append(house)

    def count_assigned_soldiers(self):
        assigned_soldiers = 0
        for house in self.houses_list:
            for room in house.rooms_list:
                for soldier in room.soldiers_list:
                    assigned_soldiers += 1

        return assigned_soldiers

    def get_info_by_person_num(self, person_num):
        for house in self.houses_list:
            for room in house.rooms_list:
                for soldier in room.soldiers_list:
                    if person_num == soldier.person_num:
                        name_house = house.name_house
                        num_room = room.name_room
                        return "Inserted", name_house, num_room
        for i in self.soldiers_without_house:
            if person_num == i.person_num:
                return "Waiting"
        return None

    def num_of_full_rooms(self):
        sum_full_rooms = 0
        for house in self.houses_list:
            for room in house.rooms_list:
                if room.is_room_full():
                    sum_full_rooms += 1
        return sum_full_rooms

    def num_of_empty_rooms(self):
        sum_empty_room = 0
        for house in self.houses_list:
            for room in house.rooms_list:
                if room.is_room_empty():
                    sum_empty_room += 1
        return sum_empty_room

    def num_of_partial_rooms(self):
        sum_partial_rooms = 0
        for house in self.houses_list:
            for room in house.rooms_list:
                if room.is_partial_room():
                    sum_partial_rooms += 1
        return sum_partial_rooms





