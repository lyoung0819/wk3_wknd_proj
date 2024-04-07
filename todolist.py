class Task():
    id_counter = 0  
    list_of_tasks = [] 

    def __init__(self, task, task_status):
        self.id_counter += 1
        self.task = task
        self.task_status = task_status

    def __str__(self):
        return f'{self.task_status} {self.task}'
    
    def __repr__(self):
        return f'<Task {self.id}|{self.task}|{self.task_status}>'

        # Define all the functions you can call against an instance of a Task
    def add(self):
        # user input to add task
        task = input('Enter new task: ')
        task_status = input('Is task complete? Y/N').lower()
        # set status of new task & add to list_of_tasks 
        if task_status == 'y':
            task_status = f'[x]'
        elif task_status == 'n':
            task_status = f'[ ]'
        else:
            print("Not a valid response. Please enter 'Y' or 'N'")
        new_task = (task, task_status)
        self.list_of_tasks.append(new_task)
        print(f'{new_task} has been added to your list!')

    def view(self):
        # make sure there are posts
        if self.list_of_tasks:
            # loop thru and print
            for task in self.list_of_tasks:
                print(task)
        else:
            #if no tasks are in list
            print('Congrats! You have no tasks on your to do list!')

    def edit_status(self, task_id):
        task = self._get_task_by_id(task_id)
        if task:
            print(f"""
            1. Task
            2. Task Status
            """)
            user_ans = input('What would you like to edit? 1 or 2? ')
            if int(user_ans) == 1:
                new_task = input('Please input new task')
                task.task = new_task
            elif int(user_ans) == 2:
                new_status = input('Is your task complete? Y/N').lower()
                if new_status == 'y':
                    new_status == '[x]'
                elif new_status == 'n':
                    new_status == '[ ]'
                else:
                    print('Please provide valid response. Y/N')
                task.task_status = new_status
            else: 
                print('Please provide a 1 or 2.')

    def delete(self, task_id):
        task = self._get_task_by_id(task_id)
        if task:
            confirmation = input('Are you sure you would like to delete this task? Y/N').lower()
            if confirmation == 'y':
                self.list_of_tasks.remove(task)
                print('{self.task} has been deleted.')
            else:
                print('{self.task} has not been deleted.')
        else:
            print('There is no task with the ID of {task_id}!')

    def _get_task_by_id(self, task_id):
        # loop through all tasks in list
        for task in self.list_of_tasks:
            if self.task.id == task_id:
                return task

    def quit(self):
        return 'Thank you for using the Task Manager. Have a great day!'


    
class TaskList():
    print('Welcome to the Task Manager!')
    newtasklist = Task()
    print(f"""
    1. Add a task
    2. View a task
    3. Edit a task or task status
    4. Delete a task
    5. Quit the program
        """)
    to_do = input('What would you like to do? Please provide the number.')
    while True:
        while to_do not in {'1', '2', '3', '4', '5'}:
            to_do = input('Not valid. Please enter 1, 2, 3, 4, or 5.')
        if to_do == '1':
            newtasklist.add()
            to_do = input('What would you like to do? Please provide the number.')
        elif to_do == '2':
            newtasklist.view()
            to_do = input('What would you like to do? Please provide the number.')
        elif to_do == '3':
            newtasklist.edit_status() 
            to_do = input('What would you like to do? Please provide the number.')
        elif to_do == '4':
            newtasklist.delete()
            to_do = input('What would you like to do? Please provide the number.')
        elif to_do == '5':
            newtasklist.quit() 
            break
       

        



