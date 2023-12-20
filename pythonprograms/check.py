#prgm to check whether a word is present or not

txt="My name is Merin Magi Telson"
if "Magi" in txt:
    print("Magi is found")

#check is not present in this text

if "he" not in txt:
    print("It is not found")

#tocheck length of the variable named txt
print(len(txt))

#slicing the variabvlr text suing starting index and ending index
print(txt[3:6])
print(txt[:4])
print(txt[8:])
print(txt[-5:-3])