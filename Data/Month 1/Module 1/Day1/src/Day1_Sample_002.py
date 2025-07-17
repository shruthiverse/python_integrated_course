# Day1_Samples_002.py

# Sample Program 1: Basic Arithmetic Operations
num1 = 10
num2 = 5
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Sample Program 2: Calculating Area of a Circle
radius = 7
pi = 3.14
area = pi * (radius ** 2)
print("Area of the Circle:", area)

# Sample Program 3: Swapping Two Variables
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)

# Sample Program 4: Simple Interest Calculation
principal = 1000
rate = 5
time = 2
interest = (principal * rate * time) / 100
print("Simple Interest:", interest)

# Sample Program 5: Checking Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
