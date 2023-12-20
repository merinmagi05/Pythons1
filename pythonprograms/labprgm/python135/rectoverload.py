class Rectangle:
    def __init__(self,length,width):
        self.l1=length
        self.w1=width
    def area(self):
        area=self.l1*self.w1
        return area
    def __lt__(self,obj):
        if self.area() < obj.area():
            return "The Area of the Rectangle 1 is lesser than Rectangle 2"
        else:
            return "The area of the Rectangle 2 is lesser than Rectangle 1"

print("RECTANGLE 1")
l=int(input("Enter the length of the Rectangle 1:"))
w=int(input("Enter the width of the Rectangle 1:"))
obj1=Rectangle(l,w)
print("Area :",obj1.area())


print("RECTANGLE 2")
l=int(input("Enter the length of the Rectangle 2:"))
w=int(input("Enter the width of the Rectangle 2:"))
obj2=Rectangle(l,w)
print("Area :",obj2.area())

print("Comparing Rectangle 1 and Rectangle 2")
print(obj1 < obj2)

