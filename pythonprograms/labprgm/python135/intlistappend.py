
n=int(input("Enter the size  of the list:"))
a=[]
#using for loop to set range
for i in range(0,n):
        c=int(input(f"Enter the {i+1}th value :"))

#applying condition to store in over
        if c>100:
                a.append("over")
        else:
                a.append(c)

#displaying the list
print(a)
