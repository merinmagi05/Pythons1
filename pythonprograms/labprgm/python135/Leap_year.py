current_yr=int(input("Enter the current year:"))
final_yr=int(input("Enter the final year:"))
print("Leap Years are:")
for i in range(current_yr,final_yr):
    if(i%4 ==0 and i%100!=0 or i%400==0):
        print(i)
