tasks = []
def add_task():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Your task '{task}' is added to the list.")

def list_task():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Tasks are:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
def delete_task():
    list_task()
    try:
        task_to_delete = int(input("Choose the task to be deleted."))
        if task_to_delete>0 and task_to_delete<=len(tasks):
            tasks.pop(task_to_delete)
            print("'{task_to_delete}' has been removed")

        else:
            print("Your Task #{task_to_delete} was not found.")


    except:
        print("Invalid Input")


if __name__ == "__main__":
    print("~~~Welcome to to-do-list python application~~~")
    while True:
        print("\n")
        print("Please select one of the following: ")
        print("---------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        print("----------------------------------------")
        
        choice = input("Enter your choice: ")

        if(choice=="1"):
            add_task()
        
        elif(choice == "2"):
            delete_task()
        
        elif(choice == "3"):
            list_task()
        
        elif(choice== "4"):
            break
        

        else:
            print("Please enter a valid input.")

    print("BYE.....BYE.....SEE YOU........👋👋👋")