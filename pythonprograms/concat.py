a="Merin "
b="Magi "
c="Telson"
d=a+b+c
print("My name is:",d)

#curly brackets are used  instead of %d
age=21
x="My name is Maggie and I am {}"
print(x.format(age))

s=45
g=2
k=256
order="I want to pay {} rupees for {} kg in id {}"
print(order.format(s,g,k))
#escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
print(txt.capitalize())