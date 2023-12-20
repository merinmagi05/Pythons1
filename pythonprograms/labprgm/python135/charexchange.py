"""Create a string from given string where first and last characters exchanged"""

gstring=str(input("Enter a string:"))
estring=gstring[-1]+gstring[1:-1]+gstring[0]
print("Characters exchanged string:",estring)