import csv
with open("csv3.csv",newline="")as csvfile:
    d=csv.DictReader(csvfile)
    print("NAME    ROll no")
    print(".................")
    for i in d:
        print(i['NAME']," ", i['ROLLNO'])