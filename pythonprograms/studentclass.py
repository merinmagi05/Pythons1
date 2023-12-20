class student:
    def __init__(self, name, sclass, rollno):
        self.n = name
        self.s = sclass
        self.r = rollno


    def printstudent(self):
        print("_STUDENT DETAILS_")
        print("your name:",self.n)
        print("your class:",self.s)
        print("your Roll Number:",self.r)

n=str(input("Enter your name: "))
s=str(input("Enter your class: "))
r=int(input("Enter your Roll Number: "))
obj=student(n,s,r)
obj.printstudent()