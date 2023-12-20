fruits = {'Apple': 2, 'Orange': 14, 'Pinapple': 45, 'Watermelon': 61, 'Grapes': 10}
l=list(fruits.items())
l.sort()
print('Ascending order is : ', l)
l=list(fruits.items())
l.sort(reverse=True)
print('Descending order is : ', l)