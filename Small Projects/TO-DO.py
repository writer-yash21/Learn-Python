#Developed by yash jangid
#Github-Link -> https://github.com/writer-yash21

from time import sleep
class Task:

    Tasks:list = []

    def ShowTask(self):
        if(len(self.Tasks) == 0):
            print("No Task")
            return
        print("Loading...")
        sleep(3)
        for task in range(0,len(self.Tasks)):
            print(f"{task+1}. -> {self.Tasks[task]}")

    def AddTask(self,task:str):
        self.Tasks.append(task)
        print("Added Sucessfully")

    def DeleteTask(self,task_no:int):
        if(task_no < 0 or task_no > len(self.Tasks)):
            print("Invalid task no.")
            return
        self.Tasks.pop(task_no-1)
        print("Delete Sucessfully")

    def UpdateTask(self,task_no:int,task:str):
        if(task_no < 0 or task_no > len(self.Tasks)):
            print("Invalid task no.")
            return
        self.Tasks[task_no-1] = task
        print("Update Sucessfully")


print("This is a Todo App")
T:object = Task()
while(True):

    print("\n1. Show All Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit App")

    num:int = int(input("Enter no. of operation -> "))

    if num == 1:
        T.ShowTask()

    elif num == 2:
        task = input("Enter task -> ")
        T.AddTask(task)

    elif num == 3:
        task_no = int(input("Enter task no. -> "))
        T.DeleteTask(task_no)

    elif num == 4:
        task_no = int(input("Enter task no. -> "))
        task = input("Enter task -> ")
        T.UpdateTask(task_no,task)

    elif num == 5:
        exit(0)

    else:
        print("You entered wrong no. Try Again")