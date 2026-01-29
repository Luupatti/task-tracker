import datetime;
from data_manager import load_data, save_data, load_highest_id, save_highest_id

def add(description):

    data = load_data()
    current_highest_id = load_highest_id()
    id = current_highest_id +1
    createdAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    

    data[id] = {
        "description": description,
        "status": "todo",
        "createdAt": str(createdAt),
        "updatedAt": str(createdAt)
    }
    save_highest_id(id)
    save_data(data)
    print(f"Task added successfully ID:{id}")


