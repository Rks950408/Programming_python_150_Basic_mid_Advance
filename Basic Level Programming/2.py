# 2. Write a Python program to swap two numbers.
# 	Description: Swapping two numbers means exchanging their values.
# 	Hint: You can swap two variables without a temporary variable using tuple unpacking in Python (a, b = b, a).

# 1st way of swapping the two number 
num1=int(input("Enter the 1st number :"))

num2=int(input("Enter the 2nd number :"))

# num1=num1+num2
# num2=num1-num2
# num1=num1-num2

# print(f"{num1} is 1st Number")
# print(f"{num2} is 2nd Number")

# 2st way of swapping the two number  tuple unpacking
# what is tuple ? tuple is immutable 

num1,num2=num2,num1
print(f"{num1} is 1st Number")
print(f"{num2} is 2nd Number")




