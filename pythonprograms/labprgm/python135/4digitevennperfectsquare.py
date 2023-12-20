
start_range=int(input("Enter the lower limit above 999:"))
if(start_range>999) and (start_range<10000):
    end_range = int(input("Enter the upper limit below 10000:"))
    if (end_range > start_range) and (end_range < 10000):
        myList = []
        for i in range(start_range, end_range + 1):
            if i % 2 == 0:
                square_root = int(i ** 0.5)
                if square_root * square_root == i:
                    myList.append(i)
        print("The list of four digit numbers in a given range with all their digits even and the number is a perfect square.:")
        print(myList)
    else:
        print("Invalid range!")

else:
    print("Invalid range!")

































"""start_range = int(input("Enter the starting range (4-digit number): "))
end_range = int(input("Enter the ending range (4-digit number): "))

if start_range < 1000 or end_range > 9999 or start_range > end_range:
    print("Invalid input range. Please enter a valid range of four-digit numbers.")
else:
    even_digit_square_numbers = []

    for num in range(start_range, end_range + 1):
        if all(int(digit) % 2 == 0 for digit in str(num)):
            square_root = int(num ** 0.5)
            if square_root * square_root == num:
                even_digit_square_numbers.append(num)

    if even_digit_square_numbers:
        print("Four-digit perfect square numbers with all even digits in the range:")
        print(even_digit_square_numbers)
    else:
        print("No such numbers found in the given range.")"""
