from data_manager import load_data


def list_all():
    data = load_data()
    for id in data:
        print ("ID:" +id, data[id])

def list_done():
    data = load_data()
    for id in data:
        if data[id]["status"] == "done":
            print ("ID:" +id, data[id])

def list_todo():
    data = load_data()
    for id in data:
        if data[id]["status"] == "todo":
            print ("ID:" +id, data[id])

def list_in_progress():
    data = load_data()
    for id in data:
        if data[id]["status"] == "in-progress":
            print ("ID:" +id, data[id])