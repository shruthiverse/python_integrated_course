# Day2_Sample_005.py

# Example 1: Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2 if num2 != 0 else "Division by zero"
else:
    result = "Invalid Operation"

print("Result:", result)

# Example 2: Finding the Largest Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is:", largest)

# Example 3: Odd or Even Checker
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# Example 4: Grading System
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

# Example 5: Simple Interest Calculator
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print("The Simple Interest is:", simple_interest)
