from data_manager import load_data, save_data
import datetime

def update(id, description):
    try:
        data = load_data()
        data[id]["description"] = description
        data[id]["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_data(data)
    except KeyError:
        print("You are trying to update a item that does not exist ID:" + id)

