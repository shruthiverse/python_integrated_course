# Day2_Sample_001.py
# Simple Calculator Program

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")

# Day2_Sample_002.py
# Check if a number is Even or Odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# Day2_Sample_003.py
# Calculate Area of a Circle

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(f"The area of the circle with radius {radius} is {area:.2f}")

# Day2_Sample_004.py
# Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Day2_Sample_005.py
# Simple Interest Calculation

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))

simple_interest = (principal * rate * time) / 100
print(f"The simple interest is {simple_interest}")
