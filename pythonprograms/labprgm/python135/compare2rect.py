
class rect:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth

    def area(self):
        self.a=self.l*self.b


    def peri(self):
        self.p=2*(self.l+self.b)

    def disp(self):
        print("Area of the rectangle:",self.a)
        print("Perimeter of the rectangle",self.b)

    def compare(self,obj2):
        if self.a==obj2.a:
            print("Areas are equal")
        elif self.a > obj2.a:
            print("Area 1 is greater than Area 2")
        else:
            print("Area 2 is greater than Area 1")

print("Rectangle 1")
l1=int(input("Enter the length of the Rectangle 1:"))
b1=int(input("Enter the breadth of the Rectangle 1:"))
print("Rectangle 2")
l2=int(input("Enter the length of the Rectangle 2:"))
b2=int(input("Enter the breadth of the Rectangle 2:"))

obj1=rect(l1,b1)
obj2=rect(l2,b2)
obj1.area()
obj1.peri()
obj2.area()
obj2.peri()
obj1.disp()
obj2.disp()
obj1.compare(obj2)