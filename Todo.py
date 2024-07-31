# tasks = []

# def addTask():
#   task = input("Please enter your task: ")
#   tasks.append(task)
#   print(f"Task '{task}' added to the list")
  
# def listTask():
#   if not tasks:
#     print("There are no tasks currently")
#   else:
#     print("Current Tasks: ")
#     for index, task in enumerate(tasks):
#       print(f"Task #{index}. {task}")

  
# def deleteTask():
#   listTask()
#   try:
#     taskToDelete = int(input("Enter the # to delete: "))
#     if taskToDelete >=0 and taskToDelete < len(tasks):
#       tasks.pop(taskToDelete)
#       print("Deleted")
#     else:
#       print(f"Not found")
#   except:
#     print("Invalid Input")

# if __name__ == "__main__":
#   print("ToDo List")
  
#   while True:
#     print("select options")
#     print("1. Add")
#     print("2. Delete")
#     print("3. List")
#     print("4. Quit")
    
#     choice = input("Enter your choice: ") 
    
#     if (choice == '1'):
#       addTask()
    
#     elif (choice == '2'):
#       deleteTask()
    
#     elif (choice == '3'):
#       listTask()

#     elif (choice == '4'):
#       break
      
#     else:
#       print("Invalid input. please try again")

#   print("Goodbye")

class ToDolist:
  def __init__(self):
    self.tasks = []
    
  def addTask(self):
    task = input("Please enter your task: ")
    self.tasks.append(task)
    print(f"Task '{task}' added to the list")
  
  def listTask(self):
    if not self.tasks:
      print("There are no tasks currently")
    else:
      print("Current Tasks: ")
      for index, task in enumerate(self.tasks):
        print(f"Task #{index}. {task}")

  
  def deleteTask(self):
    self.listTask()
    try:
      taskToDelete = int(input("Enter the # to delete: "))
      if taskToDelete >=0 and taskToDelete < len(self.tasks):
        self.tasks.pop(taskToDelete)
        print("Deleted")
      else:
        print(f"Not found")
    except:
      print("Invalid Input")

  def run(self):
    print("ToDo List")
  
    while True:
      print("select options")
      print("1. Add")
      print("2. Delete")
      print("3. List")
      print("4. Quit")
    
      choice = input("Enter your choice: ") 
    
      if (choice == '1'):
        self.addTask()
    
      elif (choice == '2'):
        self.deleteTask()
    
      elif (choice == '3'):
        self.listTask()

      elif (choice == '4'):
        break
      
    else:
      print("Invalid input. please try again")

  print("Goodbye")

todo_list = ToDolist()
todo_list.run()