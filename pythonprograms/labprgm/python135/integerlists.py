

list1=[5,7,6,8,24,54,35]
list2=[3,1,2,10,43,36,10]
print("List 1:",list1)
print("List 2",list2)
#displaying the length using len()
print("The length of List 1=",len(list1))
print("The length of the List 2=",len(list2))
#checking whether the lists are of the same length
if len(list1)==len(list2):
    print("The two Lists are of the same length.")
else:
    print("The Length of the two list are different")
#displaying the sum of the list
print("The sum of the list 1=",sum(list1))
print("The sum of the List 2=",sum(list2))
#checking the sum of two list are same or not
if sum(list1)==sum(list2):
    print("The Sum of Two list are same")
else:
    print("The Two lists sum are not same")
#checking any repeated values in list 1 and 2
check=any(item in list1 for item in list2)
print("Any value occur in both",check)