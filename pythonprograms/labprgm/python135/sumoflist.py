list=[]
num=int(input("Enter the number of elements in the list :"))
print("Enter the elements:")
for i in range(0,num):
    items=int(input())
    list.append(items)
print(list)

print("The sum of the elements of the List is : " , sum(list))