from data_manager import load_data, save_data

def delete(id):
    try:
        data = load_data()
        data.pop(id)
        save_data(data)
    except KeyError:
        print("You are trying to delete a item that does not exist ID:" + id)