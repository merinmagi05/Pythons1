thislist = ["apple", "banana", "cherry"]
flower=["rose","sunflower","jasmine","gerbera"]
name=("magi","feba","deva","kochu")
#inserting into a specific position
thislist.insert(2, "watermelon")
print(thislist)
#insertin at last
thislist.append("orange")
print(thislist)
#to append elements of another list ,or to merge them into a single list
thislist.extend(flower)
print(thislist)
#also used in tuple
thislist.extend(name)
print(thislist)
#remove is used to remove a specified item ,it removes the first occurance of the item
thislist.remove("kochu")
print(thislist)
#pop() removes the specific index,if not specifies it deletes from last
thislist.pop(7)
print(thislist)
#delete can also remove from the specified index and it can also del the whole list using the keyword del
del thislist[8]
print(thislist)
#The list still remains and it has no contents
flower.clear()
print(flower)