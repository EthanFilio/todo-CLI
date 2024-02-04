'''
Description:
This is a simple task management CLI program.
Its main functions include: add, edit, show, complete, and exit.
Tasks are stored in a txt file, allowing users to monitor their progress efficiently.
'''


def add_task(todo: str):
    with open('tasks.txt', 'a') as storage:
        storage.write(f'{todo}\n')


# Helper function
def is_within_bound(todo_index: str, todos: list):
    todo_index = int(todo_index)
    if todo_index not in range(1, len(todos) + 1):
        return False
    return True


# Helper function
def get_tasks(todos: list = None):
    if todos is None:
        with open('tasks.txt', 'r') as storage:
            return [line.strip() for line in storage.readlines()]


def edit_task(todos: list, todo_index: str):
    if is_within_bound(todo_index, todos):
        todo_index = int(todo_index)
        todos[todo_index - 1] = input('Enter edit: ')

        with open('tasks.txt', 'w') as storage:
            storage.writelines([f'{todo}\n' for todo in todos])

        show_task()

    else:
        print('Index out of bounds.')


def show_task(todos: list = None):
    if todos is None:
        todos = get_tasks()

    for i, todo in enumerate(todos, start=1):
        print(f'    {i}. {todo}', end='\n')


def complete_task(todos: list, todo_index: str):
    if is_within_bound(todo_index, todos):
        todo_index = int(todo_index)
        del todos[todo_index - 1]

        with open('tasks.txt', 'w') as storage:
            storage.writelines([f'{todo}\n' for todo in todos])

        show_task()

    else:
        print('Index out of bounds.')


while True:
    user_decision = input('Type add_(task), edit_(number of task), show, complete_(number of task), or exit: ').lower().strip()

    if user_decision.startswith('add'):
        task = user_decision[4:].strip()
        if not task:
            continue
        else:
            add_task(task)

    elif user_decision.startswith('edit'):
        try:
            tasks = get_tasks()

            if len(tasks) == 0:
                print('There are no task(s) to edit yet.')
            else:
                task_index = user_decision[5:]
                edit_task(tasks, task_index)

        except ValueError:
            print('There seems to be an error in the input. Please enter a number instead.')
            continue

    elif user_decision.startswith('show'):
        show_task()

    elif user_decision.startswith('complete'):
        try:
            tasks = get_tasks()

            if len(tasks) == 0:
                print('There are no task(s) to complete yet.')
            else:
                task_index = user_decision[9:]
                complete_task(tasks, task_index)

        except ValueError:
            print('There seems to be an error in the input. Please try again.')
            continue

    elif user_decision.startswith('exit'):
        break

    else:
        print('There seems to be an error in the input. Please try again.')
