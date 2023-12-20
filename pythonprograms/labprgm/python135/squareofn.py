mylist=[]
start=int(input("Enter the lower limit:"))
end=int(input("Enter the upper limit:"))
print("The Squares are:")
for i in range(start,end+1):
    square=i**2

    print(f"{i}={square}")
    mylist.append(square)

print("The list is:", mylist)


