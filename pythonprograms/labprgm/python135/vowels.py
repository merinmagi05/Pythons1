vowels=['A','E','I','O','U','a','e','i','o','u',]
word=input("Enter the word:")
a=[i for i in word if i in vowels]
print(a)