def reg_user(): # This function registers a user
    with open('user.txt') as f:
        print("\nEnter a new Username:")
        new_user = input()           
        if new_user in f.read():
            print("\nUsername already exists in file!")  
            reg_user()           
        else:
            print("Please enter your new password:")
            new_pass = input()
            print("Please confirm your new password:")
            confirm_pass = input()
            if confirm_pass == new_pass:
                with open('user.txt', 'a') as f:
                    f.write('\n' + new_user +', ' + new_pass)


def add_task(): # This function adds a task to the tasks file
    print("Please enter the date:")
    date = input()
    print("Enter the username of the person you assigning the task to:")
    new_task_user = input()
    print("Enter the Title of the task:")
    task_title = input()
    print('Enter the description of the task:')
    task_description = input()
    print('When is the deadline for the task?')
    task_due = input()
    complete = "NO"

    with open('tasks.txt', 'a') as f:
        f.write('\n' + new_task_user +', ')
        f.write(task_title + ", ")
        f.write(task_description + ', ')
        f.write(date + ', ') 
        f.write(task_due + ', ')
        f.write(complete)


def view_all(): #This funtion shows the user all the tasks
    with open('tasks.txt', 'r') as f:
        for line in f:            
            tasklist = line.split(", ")
            print("\nTask: "+ tasklist[1])
            print("Assigned to: "+ tasklist[0])
            print('Date assigned: '+ tasklist[3])
            print("Due date: "+ tasklist[4])
            print("Task complete? NO")
            print("Task description: " + tasklist[2])
                

def view_mine(): # This funtion allows the user to view and edit their task
    task_Dict = {} # an empty dictionary is made
    with open('tasks.txt', 'r') as f: # the task file is opened to read from
        task_num = 1 # variable that holds the number the line the task is on 
        for line in f: # going through each line in the task file
            tasklist = line.split(", ") # isolate every piece of info between the space and comma
            task_Dict[task_num] = line # addind info to the empty dictionary (the number line and the info on the line) 
            
            if user == tasklist[0]: # this checks if the user exists in the task file. the usersname is always the first index.
                print("\nTask Number: "+ str(task_num) + '\n') #displays the line the users task is on in the task file.
            # the following is all the infomation in the line with the users name
                print("Task: "+ tasklist[1]) 
                print("Assigned to: "+ tasklist[0])
                print('Date assigned: '+ tasklist[3])
                print("Due date: "+ tasklist[4])
                print("Task complete? NO")
                print("Task description: " + tasklist[2])
            task_num += 1 # number is iterated for every line and stores the number line the users task is on                     

        user_edit_task = int(input(f"\nwhich task would you like to edit?\nTask Number: ")) # user inputs the task they want to edit
        print(task_Dict[user_edit_task]) 
        print("\nPlease select one of the following:")
        print("m - Mark task as complete")
        print('e - Edit the task')
        print('-1 - Return to main menu')
        edit_task = input("Enter your letter selection here: ")
        if edit_task == '-1':
            return 
        if edit_task == 'm':
            mark_line = task_Dict[user_edit_task].split(', ') # split the dictionary using the comma and space as seperator
            mark_line[-1] =  "YES\n" # change the data on the last index
            print("Task marked as completed.")                 
            task_Dict[user_edit_task] = ", ".join(mark_line) # join the new change to the original dictionary
        
        elif edit_task == 'e':
            print('\neu - Edit username')
            print('dd - Edit due date')
            edit_task_1 = input("Enter your letter selection here: ")
            if edit_task_1 == 'eu':
                print(f"\nCurrent username: {user}")
                mark_line = task_Dict[user_edit_task].split(', ')
                mark_line[0] =  input("Enter new username:\n")
                print(mark_line)
            elif edit_task_1 == 'dd':
                print(f"\nCurrent Deadline: {tasklist[4]}")
                mark_line = task_Dict[user_edit_task].split(', ')
                mark_line[4] =  input('Enter new due date:\n')
                print(mark_line)

        dataTasks = '' # make an empty string
        for t in task_Dict.values(): # returns all the values in the dictionary
            dataTasks += t   # puts the values into a string format, with the new change
        # print(dataTasks)
        with open('tasks.txt', 'w') as f:
            f.write(dataTasks) # overwrite the string in the txt file with the new string


def display_statistics(): # this funtion shows the admin all the data from the user_overview file and the tasks_overview file.
        with open('task_overview.txt', 'r') as f: #open task file in read mode
           print('\n' + f.read() + '\n')
        with open('user_overview.txt', 'r') as uf:
            print(uf.read() + '\n')


def completed_tasks(): # This funtion writes the total number of completed tasks to the file
    with open('tasks.txt', 'r') as read_f: # open file i want to read from
        a = 0
        for line in read_f.readlines():
            strip_Newline = line.strip('\n') # remove newline character from string
            split_line = strip_Newline.split(', ')     # split the string into a list          
            if split_line[-1] == 'YES': # completion of tasks is always the last index.
                a += 1                   # program will count how many 'YES' there are
        total = a
        with open('task_overview.txt', 'w') as write_f:
            write_f.write(f"Number of completed tasks in file: {total} task/s completed") #open a new file to write data into
            # print(f"\nNumber of completed tasks in file: {total} task/s completed")


def uncompleted_tasks(): # This funtion writes the total number of incompleted tasks to the file
    with open('tasks.txt', 'r') as read_f:
        a = 0
        for line in read_f:
            strip_Newline = line.strip('\n')
            split_line = strip_Newline.split(', ')
            if split_line[-1] == "NO": # program will count how many 'NO' there are
                a += 1
        total = a
        with open('task_overview.txt', 'a') as write_f:
            write_f.write(f"\nNumber of incompleted tasks in file: {total} task/s completed")
            # print(f"Number of incompleted tasks in file: {total} task/s completed")


def overdue_task(): #This funtion writes the total number of overdue tasks to the file
    with open('tasks.txt', 'r') as read_f:
        a = 0
        for line in read_f:
            strip_Newline = line.strip('\n')
            split_line = strip_Newline.split(' ')
            due_date = int(split_line[-4]) # dates have a fixed format and therefore are idexed from the same spot everytime
            assigned_date = int(split_line[-7]) 
            if due_date < assigned_date: # if the second date is bigger than the first, than the task is incomplete
                a += 1
        with open('task_overview.txt', 'a') as write_f:
            write_f.write(f"\nIncompleted tasks Overdue: {a} task/s overdue")   #number is appended to the file
            # print(f"Incompleted tasks Overdue: {a} task/s overdue")


def percentage_incomplete(): #This funtion writes the total percentage of incomplete tasks to the file
    with open('tasks.txt', 'r') as read_f:
        a = 0
        b = 0
        for line in read_f:
            b += 1 # gets the total number of lines
            strip_Newline = line.strip('\n')
            split_line = strip_Newline.split(', ')
            if split_line[-1] == "NO": # program will count how many 'NO' there are
                a += 1
        percentage = round((a/b) * 100) # method to calculate percentage of incomplete tasks
        with open('task_overview.txt', 'a') as write_f:
            write_f.write(f"\nPecentage of incomplete tasks: {percentage}% of task/s incomplete.")
        # print(f"Pecentage of incomplete tasks: {percentage}% of task/s incomplete.")


def percentage_overdue(): #This funtion writes the total percentage of complete tasks to the file
    with open('tasks.txt', 'r') as read_f:
        a = 0
        b = 0
        for line in read_f:
            b += 1
            strip_Newline = line.strip('\n')
            split_line = strip_Newline.split(' ')
            due_date = int(split_line[-4]) 
            assigned_date = int(split_line[-7]) 
            if due_date < assigned_date: 
                a += 1
        percentage = round((a/b), 2) * 100
        with open('task_overview.txt', 'a') as write_f:
            write_f.write(f"\nPecentage of overdue tasks: {percentage}% task/s currently overdue.")
        # print(f"Pecentage of overdue tasks: {percentage}% task/s currently overdue.")


def total_users_tasks(): # this function calculates the total users in the user.txt file
    with open('user.txt', 'r') as f: 
        a = 0
        for line in f:
            line.split(', ')
            a += 1

        with open('user_overview.txt', 'w') as write_f: # new user file is opened and written to
            write_f.write(f"Total users and tasks in user file: {a} users and {a} tasks.")
            # print(f"Total users and tasks in user file: {a} users and {a} tasks.")


def generate_reports(): # This function calls all the appropriate functions when the user inputs 'gr'
    completed_tasks()
    uncompleted_tasks()
    overdue_task()
    percentage_incomplete()
    percentage_overdue()
    total_users_tasks()
    user_overview()

    with open('task_overview.txt', 'r') as f:
        print('\n' + f.read() + '\n')


def user_overview():
    #count the number of users and the number of task
    # add a code to find the number of task
    with open('tasks.txt', 'r') as f: #count the number of tasks in the task file
            numb_task = 0
            for line in f.readlines():
                numb_task += 1 
            print(f"\nThere are a total of {numb_task} tasks in your tasks.file.")

    with open('user.txt', 'r') as f:   #count the number of users in the user file    
            user_name = 0
            for line in f.readlines():
                user_name += 1
            print(f"There are a total of {user_name} users in your user.file.\n")

    user_data = ''
    with open("user.txt", "r") as usf:
        for line in usf:
            us_name = line.split(", ")
            user_data += user_info(us_name, numb_task)

    print(user_data)
    with open('user_overview.txt' , 'w') as write_f:
        write_f.write(f"There are a total of {numb_task} tasks in your tasks.file.\n")
        write_f.write(f"There are a total of {user_name} users in your user.file.\n\n")
        write_f.write(user_data)


def user_info(user_name, num_task): # This funtion write the data for each user to a file called 'user_overview.txt'
    with open('tasks.txt', 'r') as f: 
        user_tasks = 0
        user_tasks_complete = 0
        user_tasks_Notcomplete = 0
        task_overdue = 0
        percentage_OfTotal = 0
        percentage_OfComplete = 0
        percentage_OfNot_Complete = 0
        for line in f:
            list_oftasks = line.split(', ') # get every element in the line seperated
            # print(list_oftasks)
            if user_name == list_oftasks[0]: # when the user-name appears in the file the task number is incremented
                user_tasks += 1              
                if list_oftasks[-1] == 'YES\n': # check if the task is completed
                    user_tasks_complete += 1
                    if list_oftasks[-1] == 'NO\n': # check if the task is incomplete.
                        user_tasks_Notcomplete += 1
                    for line in f:
                        list_oftasks = line.strip('\n')
                        split_list_oftasks = list_oftasks.split(' ')
                    b = int(split_list_oftasks[-7]) # the date the task was assigned
                    a = int(split_list_oftasks[-4]) #the date the task is due
                    if  a < b: # if the task due date is greater than the task assigned date than its still within deadline and is not overdue.
                        task_overdue += 1

                percentage_OfTotal = round(user_tasks/num_task * 100) #percentage of tasks assigned to user
                percentage_OfComplete = round((user_tasks_complete/user_tasks * 100),2 ) #percentage of users tasks that are complete
                percentage_OfNot_Complete = round((user_tasks_Notcomplete/user_tasks * 100),2 ) #percentage of users tasks that are not complete


        per_user = f"{user_name} assigned with {user_tasks} tasks."      
        per_user += f"\n{percentage_OfTotal}% of all tasks have been assigned to {user_name}."
        per_user += f"\n{user_name} has completed {percentage_OfComplete}% of their tasks"
        per_user += f"\n{user_name} still has {percentage_OfNot_Complete}% of their tasks left to complete."
        per_user += f'\n{user_name} has {percentage_OfComplete}% of tasks completed and has {task_overdue} task/s overdue.\n\n'
        return per_user


try_again = 'y'
user = ""
while try_again == 'y':

    print("\nLOGIN")
    user = input("Enter Login username: ")
    password = input("Enter Login password: ")
    credentials = str(user) + ", " + str(password)
    with open('user.txt', 'r') as f:
        for line in f.readlines():
            if line.strip('\n') == credentials: 
                try_again = 'n'
                break 

        if try_again == 'y':
            print("\nWrong Login entered.\nPlease try again.") 

        else:     
            print(f"\nWelcome {user}.")             
            
if user == "admin":
    print("\nPlease select one of the following options: ")
    print("r - Register user")
    print('a - Add task')
    print('va - View all tasks')
    print('vm - View my tasks')
    print("gr - Generate reports")
    print("ds - Display statistics")
    print('e - Exit')
else:
    print("\nPlease select one of the following options; ")
    print('a - add task')
    print('va - view all tasks')
    print('vm - view my tasks')
    print('e - exit')

select = input("Enter your letter selection here: ")

selection = select.lower()

if selection == 'r' and user == "admin":
    reg_user()

if selection == 'a':
    add_task()

if selection == 'va': 
    view_all()

if selection == 'vm': 
    view_mine()
    
if selection == 'ds':
    display_statistics()

if selection == 'gr':
    generate_reports()