str1=str(input("Enter first string:"))
str2=str(input("Enter second string:"))
print("The entered string is:",str1+" "+str2)
s=str2[:1]+str1[1:]
s1=str1[:1]+str2[1:]
print("The new string is:",s+" "+s1)