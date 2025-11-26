from house import House


class Basis:
    def __init__(self,city, houses = 2, name = "Shivat hashibolim"):
        self.city = city
        self.houses = houses
        self.name = name
        self.houses_list = []

    def add_house(self, house: House):
        if len(self.houses_list) == self.houses:
            raise
        self.houses_list.append(house)

    def count_assigned_soldiers(self):
        assigned_soldiers = 0
        for house in self.houses_list:
            for room in house:
                for soldier in room:
                    assigned_soldiers += len(soldier)

        return assigned_soldiers



