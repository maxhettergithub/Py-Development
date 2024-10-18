tasks = []

def addTask():
    task = input("Please enter a task you want to complete: ")
    tasks.append(task)
    print(f"Task {task} has been added to the list.")


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
            listTask()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")   
    
    print("Goobbye")