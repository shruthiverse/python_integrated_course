# Day2_Sample_001.py
# (Examples as created before)

# Day2_Sample_002.py
# (Examples as created before)

# Day2_Sample_003.py
# (Examples as created before)

# Day2_Sample_004.py
# (Examples as created before)

# Day2_Sample_005.py
# 1. Linear Search
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter number to search: "))
found = False
for num in numbers:
    if num == target:
        found = True
        break

if found:
    print(f"{target} found in the list.")
else:
    print(f"{target} not found in the list.")

# 2. Bubble Sort
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(f"Sorted list: {numbers}")

# 3. Matrix Addition
matrix1 = [[int(input(f"Enter value for Matrix1 [{i}][{j}]: ")) for j in range(2)] for i in range(2)]
matrix2 = [[int(input(f"Enter value for Matrix2 [{i}][{j}]: ")) for j in range(2)] for i in range(2)]
result = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]
print("Resultant Matrix:")
for row in result:
    print(row)

# 4. Counting Words in a String
text = input("Enter a sentence: ")
words = text.split()
print(f"Number of words: {len(words)}")

# 5. Temperature Conversion (Fahrenheit to Celsius)
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is {celsius}°C.")
