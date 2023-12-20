n = int(input("Enter the limit:"))

a, b = 0, 1
for i in range(n):
    if i <= 1:
        result = i
    else:
        result = a + b
        a, b = b, result
    print(result)