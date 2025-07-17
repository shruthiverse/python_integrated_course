# Day1_Samples_005.py

# Sample Program 1: Simple Calculator using Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

# Sample Program 2: Factorial of a Number
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial of", n, "is", factorial)

# Sample Program 3: Palindrome Checker
text = input("Enter a string: ")
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# Sample Program 4: Fibonacci Series
n_terms = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b

# Sample Program 5: Prime Number Checker
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
