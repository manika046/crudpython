class ExpenseTracker:
  def __init__(self):
    self.expensetracker = []
    
  def add(self):
    date = input("Enter the date (YYYY/MM/DD): ")
    amount = input("Enter Amount")
    
    for expense in self.expensetracker:
      if expense['date'] == date:
        expense['amount'] += amount
        print("Amount Added and Updated!")
        return
      
    expense = {'date': date, 'amount': amount}
    self.expensetracker.append(expense)
    
    print("Added Successfully!")
    
  def view(self):
    print("\n Date \t\t Amount")
    for expense in self.expensetracker:
      print(f"{expense['date']} \t\t {expense['amount']}")
    
tracker = ExpenseTracker()

while True:
  print("select options")
  print("1. Add")
  print("2. View")
  print("3. Go Back")
    
  choice = input("Enter your choice: ") 
    
  if (choice == '1'):
    tracker.add()
    
  elif (choice == '2'):
    tracker.view()
        
  elif (choice == '3'):
    break
      
  else:
    print("Invalid input. please try again")