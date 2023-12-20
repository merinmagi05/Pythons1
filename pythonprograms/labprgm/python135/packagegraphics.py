from graphics.dgraphics import cuboid,sphere
from graphics import circle,rectangle

#circle
r=int(input("Enter the radius of the circle:"))
circle.areac(r)
circle.peric(r)
#rectangle
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
rectangle.arear(l,b)
rectangle.perir(l,b)
#cuboid
l1=int(input("Enter the length of the cuboid:"))
b1=int(input("Enter the breadth of the cuboid:"))
h1=int(input("Enter the height of the cuboid:"))
cuboid.areacub(l1,b1,h1)
cuboid.pericub(l1,b1,h1)
cuboid.lareacub(l1,b1,h1)
#sphere
r1=int(input("Enter the radius of the sphere:"))
sphere.areas(r1)
sphere.Diameters(r1)

