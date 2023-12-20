class Time:
    def __init__(self,hour,minute,second):
        self.h=hour
        self.m=minute
        self.s=second

    def __add__(self,obj):
        sumh=self.h + obj.h
        summ=self.m + obj.m
        sums=self.s + obj.s

        if sums > 60:
            sums=sums-60
            summ=summ+1
        if summ > 60:
            summ=summ-60
            sumh=sumh+1
        print(sumh,":",summ,":",sums)

print("TIME 1")
h1=int(input("Enter the hour :"))
m1=int(input("Enter the minute :"))
s1=int(input("Enter the seconds:"))
obj1=Time(h1,m1,s1)

print("TIME 2")
h2 = int(input("Enter the hour :"))
m2 = int(input("Enter the minute :"))
s2 = int(input("Enter the seconds:"))
obj2 = Time(h2, m2, s2)
print("The sum of two times are:")
obj1+obj2
