todos = []

def menu():
    options = """
    For adding a Todo, press 'a'
    For showing the list of Todos, press 'l'
    To mark any Todo as complete, press 'm'
    To quit, press 'q'
    """
    while True:
        choose_option = input(options).lower()
        if choose_option == 'a':
            add_todos()
        elif choose_option == 'l':
            show_todos()
        elif choose_option == 'm':
            mark_complete_todo()
        elif choose_option == 'q':
            break
        else:
            print("Invalid Input, Please Try Again! \n")

def add_todos():
    todo_name = input("Write Your Todo Name Here: ")
    todo_description = input('Write Your Todo Description Here: ')

    todos.append({
        'todo_name': todo_name,
        'todo_description': todo_description,
        "marked": "No"
    })

def show_todos():
    if not todos:
        print("No Todos available.")
    for todo in todos:
        print(todo)

def mark_complete_todo():
    search_todo_name = input("Write Todo Name Here You want to mark as Complete: ")

    for todo in todos:
        if todo['todo_name'] == search_todo_name:
            todo['marked'] = "Yes"
            print(f"Marked '{search_todo_name}' as complete.")
            break
    else:
        print(f"Todo named '{search_todo_name}' not found.")

menu()
