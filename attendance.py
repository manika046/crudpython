class Attendance:
  def __init__(self):
    self.attendance = {}  
  
  def add_student(self):
    name = input("Enter student name: ")
    if name in self.attendance:
      print("Student already exists.")
    else:
      self.attendance[name] = []
      print("Student added successfully.")

  def mark_attendance(self):
    name = input("Enter student name: ")
    if name not in self.attendance:
      print("Student not found.")
    else:
      date = input("Enter date (YYYY-MM-DD): ")
      if date in self.attendance[name]:
        print("Attendance already marked for this date.")
      else:
        self.attendance[name].append(date)
        print("Attendance marked successfully.")

  def view_attendance(self):
    name = input("Enter student name: ")
    if name not in self.attendance:
      print("Student not found.")
    else:
      print(f"Attendance record for {name}: {self.attendance[name]}")
    
  def display_menu(self):
    
    while True:
      print("\nAttendance Management System")
      print("1. Add Student")
      print("2. Mark Attendance")
      print("3. View Attendance")
      print("4. Exit")
        
      choice = input("Enter your choice: ")
        
      if choice == '1':
        self.add_student()
      elif choice == '2':
        self.mark_attendance()
      elif choice == '3':
        self.view_attendance()
      elif choice == '4':
        print("Exiting...")
        break
      else:
        print("Invalid choice. Please try again.")
def main():
  system = Attendance()
  system.display_menu()

if __name__ == "__main__":
  main()
