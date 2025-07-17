# Day1_Samples_004.py

# Sample Program 1: Basic Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Sample Program 2: Checking Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Sample Program 3: Finding the Largest Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("The largest number is:", max(a, b, c))

# Sample Program 4: Counting Vowels in a String
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print("Number of vowels:", count)

# Sample Program 5: Reversing a String
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
