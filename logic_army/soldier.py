class Soldier:
    def __init__(self, person_num: int, f_name: str,l_name: str,
                 gender: str, city: str, far_to_basis: int):
        self.person_num = person_num
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.city = city
        self.far_to_basis = far_to_basis
        self.status = ""

    def change_status(self, status):
        if status not in ["Inserted", "Waiting"]:
            raise
        self.status = status

