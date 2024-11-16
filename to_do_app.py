task_list = []

def addTask():
    task = input("Please enter a task you want to complete: ")
    task_list.append(task)
    print(f"Task '{task}' has been added to the list.")

def listTasks():
    if not task_list:
        print("There are no tasks currently.")
    else: 
        print("Here are your current tasks: ")
        for index, task in enumerate(task_list):
            print(f"Task # {index}. {task}")

def deleteTask():
    listTasks()
    if task_list:       
        try:
            taskToDelete = int(input("Enter the # to delete: "))
            if taskToDelete >= 0 and taskToDelete < len(task_list):
                task_list.pop(taskToDelete)
                print(f"Task #{taskToDelete} has been removed.")
                listTasks()
            else:
                print(f"Task #{taskToDelete} was not found.")    
        except:
            print("Invalid input.")
    else:
        return

if __name__ == "__main__":
    # Create Loop to Run App
    print("Welcome to the To-Do List App")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("-------------------------------------------")
        print("1: Add a New Task")
        print("2: Delete a Task")
        print("3: List Tasks")
        print("4: Quit")       

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")   
    
    print("Goodbye")