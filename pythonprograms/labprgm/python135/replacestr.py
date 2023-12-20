"""Get a string from an input string where all occurrences of first character replaced with
‘$’, except first character."""

a=str(input("Enter a string:"))
firstchar=a[0]
a=a.replace(firstchar,'$')
a=a+firstchar[1:]
print(a)
