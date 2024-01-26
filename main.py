while True:
    user_decision = input('Type add_(task), edit_(number of task), show, complete_(number of task), or exit: ').lower().strip()

    if user_decision.startswith('add'):
        task = user_decision[4:] + '\n'
        with open('tasks.txt', 'a+') as file:
            file.seek(0)
            tasks = file.readlines()
            file.seek(0)
            file.truncate()
            tasks.append(task)
            file.writelines(tasks)

    elif user_decision.startswith('edit'):
        try:
            with open('tasks.txt', 'a+') as file:
                file.seek(0)
                tasks = file.readlines()

            if len(tasks) == 0:
                print('There are no task(s) to edit yet.')
            else:
                task_index = int(user_decision[5:])
                if 1 <= task_index <= len(tasks):
                    tasks[task_index - 1] = input('Edit: ') + '\n'
                    with open('tasks.txt', 'w') as file:
                        file.writelines(tasks)
                else:
                    print('Number is beyond the current index')

                file.close()
        except ValueError:
            print('There seems to be an error in the input. Please try again.')
            continue

    elif user_decision.startswith('show'):
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        for index, task in enumerate(tasks, start=1):
            print(f'    {index}. {task}', end='')

    elif user_decision.startswith('complete'):
        try:
            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()

            if len(tasks) == 0:
                print('There are no task(s) to complete yet.')
            else:
                task_index = int(user_decision[9:])
                if 1 <= task_index <= len(tasks):
                    del tasks[task_index - 1]
                    with open('tasks.txt', 'w') as file:
                        file.writelines(tasks)
                else:
                    print('Number is beyond the current index')
        except ValueError:
            print('There seems to be an error in the input. Please try again.')
            continue

    elif user_decision.startswith('exit'):
        break

    else:
        print('There seems to be an error in the input. Please try again.')
