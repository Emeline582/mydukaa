class BankAccount:
   def __init__(self,account_no,balance,owner_name,open_date):
      self.account_no = account_no
      self.balance = balance
      self.owner_name = owner_name
      self.open_date = open_date

   def deposit(self,amount):
         self.balance += amount
         print(f"{self.owner_name} deposited {amount}")

   def check_balance(self,balance):
         print(f"Your balance is{balance} ")

   def withdraw(self,amount):
         if self.balance >=amount:
            self.balance -= amount 
            print( "Your withdrawal was successful")
         else :
            print("balance is insufficient")
         

      
   def get_details(self):
         print("user details")
         print(f"Account_no:{self.account_no},balance:{self.balance},Name:{self.owner_name}, open_date:{self.open_date}")
         print("_______________________________")
      
def close_account(self):
        self.closed = True
        print(f"Account {self.account_number} has been closed.")


         
#object1
customer1 = BankAccount(1788800,50000,'Juma',12/6/2020)
customer1.deposit(20000)
customer1.check_balance(70000)
customer1.withdraw(10000)
customer1.get_details()
customer1.close_account()