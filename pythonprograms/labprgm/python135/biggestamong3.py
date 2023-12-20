#Find biggest of 3 numbers entered.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter Third number:"))
if a>b and a>c:
    print(f"{a} is greater than {b} and {c}")
elif b>a and b>c:
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")
