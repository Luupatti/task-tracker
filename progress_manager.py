from data_manager import load_data, save_data
import datetime


def mark_in_progress(id):

    data = load_data()
    if not id in data:
            print("You are trying to change status from a item that does not exist ID:" + id)
            return
    data[id]["status"] = "in-progress"
    data[id]["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(data)
def mark_done(id):
    try:
        data = load_data()
        if not id in data:
            print("You are trying to change status from a item that does not exist ID:" + id)
            return
        data[id]["status"] = "done"
        data[id]["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_data(data)
    except KeyError:
        print("You are trying to change status from a item that does not exist ID:" + id)