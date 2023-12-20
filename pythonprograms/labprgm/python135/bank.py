class bank:
    def __init__(self,accountnumber,name,acctype,balance):
        self.acc=accountnumber
        self.n=name
        self.t=acctype
        self.b=balance


    def deposit(self,amount1):
        self.b+=amount1
        print("Balance=",self.b)

    def withdraw(self,amount2):
        if self.b < amount2:
            print("Invalid Amount")
        else:
            self.b+=amount2
            print("Balance after Withdrawal:",self.b)


    def display(self):
        print("Account Number:",self.acc)
        print("Name:",self.n)
        print("Account Type:",self.t)
        print("Current Balance:",self.b)


acc=int(input("Enter the Account number:"))
n=str(input("Enter name:"))
t=str(input("Enter the Account type :"))
b=int(input("Enter the Balance:"))

obj1=bank(acc,n,t,b)
obj1.display()

amount1=int(input("Enter the amount to deposit:"))
obj1.deposit(amount1)

amount2=int(input("Enter the amount to withdraw:"))
obj1.withdraw(amount2)





