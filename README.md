This is a task tracker. This can track your tasks and manage them.
commands:

add: it takes a argument: "description" of the task you want add. Example: "Making a cool app"
it will tell you if you succesfully added a task like this "Task added successfully ID(task unique id)"

update: it takes a argument: "ID" it is the tasks unique id and a second argument "description" its the new description that the task will have. Example: "Making a cool app in python" and it will also update updatedAt timestamp to current time

delete: it takes a argument: "ID" it is the tasks unique id that you want remove

mark-in-progress: it takes a argument: "ID" it is the tasks unique id that you want mark in progress

mark-done: it takes a argument: "ID" it is the tasks unique id that you want mark done

list: it takes an optional argument "done", "todo", "in-progress" if no optional argument were given it will list all the tasks like this:
ID:5 {'description': 'Making a cool app in python', 'status': 'in-progress', 'createdAt': '2026-01-29 13:30:26', 'updatedAt': '2026-01-29 13:30:26'}
ID:6 {'description': 'going for a run', 'status': 'done', 'createdAt': '2026-01-29 14:41:26', 'updatedAt': '2026-01-29 14:41:26'}
ID:9 {'description': 'cleaning', 'status': 'todo', 'createdAt': '2026-01-29 17:32:00', 'updatedAt': '2026-01-29 17:32:00'}

if optional argument were given it will show based on what optional argument was given only those tasks that match the status for example if "todo" was given it would only show those that has 'status': 'todo'...
