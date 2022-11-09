class Accounts:
        def __init__(self, balance, name):
            self.balance = balance
            self.name = name
        def credit(self,balance, deposit):
                self.balance = balance + deposit
        def debit(self,balance,withdrawal):
                self.balance = balance - withdrawal
        def get_balance(self):
            return self.balance
        def get_name(self):
            return self.name
        def set_name(self,name):
            self.name = name
            
Customer = Accounts(0, "Kituuka Bob")
print(Customer.get_name(), "has a balance of ", Customer.get_balance())
Customer.credit(500,100)
print(Customer.get_name(), "has a balance of ", Customer.get_balance())
Customer.debit(100,55)
print(Customer.get_name(), "has a balance of ", Customer.get_balance())
Customer.set_name("Wanula Jacob")
print(Customer.get_name(), "has a balance of ", Customer.get_balance())
