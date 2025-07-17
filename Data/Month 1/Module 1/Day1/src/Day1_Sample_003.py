# Day1_Samples_003.py

# Sample Program 1: Fahrenheit to Celsius Conversion
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in Celsius:", celsius)

# Sample Program 2: Sum of Natural Numbers
n = int(input("Enter a number: "))
sum_n = n * (n + 1) // 2
print("Sum of first", n, "natural numbers is:", sum_n)

# Sample Program 3: Multiplication Table
num = int(input("Enter a number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Sample Program 4: Calculating BMI
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

# Sample Program 5: Square Root Calculation
number = float(input("Enter a number: "))
square_root = number ** 0.5
print("Square root of", number, "is", square_root)
