class BankAccount:
          def __init__(self):
                      self.account_balance = 0

          def __init__(self, account_balance):
                      try:  # Check if account_balance is numeric
                              if account_balance < 0 or not isinstance(account_balance, (int, float)):
                                  raise ValueError("Account balance must be non-negative and numeric.")
                      except ValueError as e:
                                        self.account_balance = 0   
                      else:
                                        self.account_balance = account_balance

#Implement deposit(amount), withdraw(amount), and display_balance() methods.
          def deposit(self, amount):
                       try:  # Check if account_balance is numeric
                              if amount < 0 or not isinstance(amount, (int, float)):
                                  raise ValueError("Amount must be non-negative and numeric.")
                       except ValueError as e:
                                        amount = 0   
                       else:
                                        self.account_balance += amount
                      

#Create a withdraw(amount) method that returns True if the withdrawal was successful and False if the account balance is insufficient.
          def withdraw(self, amount):
                       try:  # Check if account_balance is numeric
                              if amount < 0 or not isinstance(amount, (int, float)):
                                  raise ValueError("Amount must be non-negative and numeric.")
                       except ValueError as e:
                                        amount = 0   
                       else:
                                        if self.account_balance - amount < 0:
                                             return False
                                        else:
                                             self.account_balance -= amount
                                             return True  

  
          def display_balance(self):
                  print(f"Current Balance: ${self.account_balance}")
                          