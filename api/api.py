import csv
import uvicorn
from logic_army.room import Room
from logic_army.soldier import Soldier
from fastapi import UploadFile, FastAPI, File, HTTPException
import io
from logic_army.basis import Basis
from logic_army.house import House

app = FastAPI()

def upload_csv(file_csv: bytes):
    csv_text = file_csv.decode('utf-8')
    csv_reader = csv.DictReader(io.StringIO(csv_text))
    list_info = []
    for i in csv_reader:
        list_info.append(i)
    for i in range(len(list_info) - 1):
        for j in range(len(list_info) - i - 1):
            if int(list_info[j]["מרחק מהבסיס"]) < int(list_info[j + 1]["מרחק מהבסיס"]):
                list_info[j], list_info[j + 1] = list_info[j + 1], list_info[j]
    return list_info

def create_basis(list_all_soldier: list):
    list_soldier = list_all_soldier[:]
    soldier_inserted = []
    basis = Basis()
    house1 = House("Dorm A")
    for house in range(house1.num_rooms):
        room = Room(house + 1)
        for soldier in list_soldier:
            soldier_obj = Soldier(soldier["מספר אישי"], soldier["שם פרטי"], soldier["שם משפחה"], soldier["מין"], soldier["עיר מגורים"], soldier["מרחק מהבסיס"])
            try:
                soldier_obj.status = "Inserted"
                room.add_soldiers(soldier_obj)
                list_soldier.remove(soldier)
                soldier_inserted.append(soldier)
            except:
                continue
        house1.add_room(room)

    house2 = House("Dorm B")
    for house in range(house2.num_rooms):
        room = Room(house + 11)
        for soldier in list_soldier:
            soldier_obj = Soldier(soldier["מספר אישי"], soldier["שם פרטי"], soldier["שם משפחה"], soldier["מין"], soldier["עיר מגורים"], soldier["מרחק מהבסיס"])
            try:
                soldier_obj.status = "Inserted"
                room.add_soldiers(soldier_obj)
                list_soldier.remove(soldier)
                soldier_inserted.append(soldier)
            except:
                continue
        house2.add_room(room)

    basis.add_house(house1)
    basis.add_house(house2)
    return basis, list_soldier, soldier_inserted

def create_soldiers_waiting(data_soldier: list, basis: Basis):
    new_list_solider_obj = []
    for soldier in  data_soldier:
        soldier_obj = Soldier(soldier["מספר אישי"], soldier["שם פרטי"], soldier["שם משפחה"], soldier["מין"], soldier["עיר מגורים"], soldier["מרחק מהבסיס"])
        soldier_obj.change_status("Waiting")
        new_list_solider_obj.append(soldier_obj)
        basis.soldiers_without_house.append(soldier_obj)
    return new_list_solider_obj

def info_of_soldier(soldier_waiting, soldier_inserted, basis: Basis):
    info = []
    for soldier in soldier_inserted:
        soldier_info = basis.get_info_by_person_num(soldier["מספר אישי"])
        info.append({"name": soldier["שם פרטי"],"person_number":soldier["מספר אישי"], "status": soldier_info[0], "name house": soldier_info[1], "num room": soldier_info[2]})
    for soldier in soldier_waiting:
        soldier_info = basis.get_info_by_person_num(soldier["מספר אישי"])
        info.append({"name": soldier["שם פרטי"],"person_number":soldier["מספר אישי"],"status": soldier_info})
    return info

basis = ""
@app.post("/assignWithCsv")
async def post_data(file: UploadFile = File(...)):
    global basis
    read_file = await file.read()
    data = upload_csv(read_file)
    init_basis = create_basis(data)
    create_soldiers_waiting(init_basis[1], init_basis[0])
    basis = init_basis[0]
    return [{
        "The number of soldiers assigned to rooms": init_basis[0].count_assigned_soldiers(),
        "The soldiers who remained on the waiting list are": len(init_basis[1])
    },info_of_soldier(init_basis[1],init_basis[2], init_basis[0])]


@app.get("/space")
def get_space():
    return {
        "Number of full rooms": basis.num_of_full_rooms(),
        "Number of empty rooms": basis.num_of_empty_rooms(),
        "Number of half rooms": basis.num_of_partial_rooms()
    }

@app.get("/waitingList")
def get_waiting_soldier():
    return {
        "The soldiers who were not assigned are": basis.soldiers_without_house
    }

@app.get("/search")
def get_by_person_number(person_number):
    try:
        result = basis.get_info_by_person_num(person_number)
        return {"status": result[0], "name house": result[1], "num room": result[2]}
    except:
        raise HTTPException(status_code=404, detail="person number not found")



uvicorn.run(app)
