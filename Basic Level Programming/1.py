# 1. Write a Python program to check if a number is even or odd.
# 	Description: A basic program to check if a number is divisible by 2 (even) or not (odd).
# 	Hint: Use the modulus operator % to check for divisibility (num % 2).
# Take the user input from the user all things should be dynamic .


num= int(input("Enter the number :"))

if num % 2== 0:
    
    print(f"{num} is Even Number")
else:
    print (f"{num} is Odd Number")
