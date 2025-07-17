# Day2_Sample_003.py - More Examples

# Example 1: Accessing List Elements
fruits = ['apple', 'banana', 'cherry']
print('First fruit:', fruits[0])
print('Last fruit:', fruits[-1])

# Example 2: Modifying List Elements
numbers = [1, 2, 3, 4, 5]
numbers[2] = 10
print('Modified List:', numbers)

# Example 3: Adding and Removing Elements
languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
languages.remove('Java')
print('Updated Languages:', languages)

# Example 4: List Slicing
colors = ['red', 'green', 'blue', 'yellow', 'purple']
sliced_colors = colors[1:4]
print('Sliced Colors:', sliced_colors)

# Example 5: List Comprehension
squares = [x ** 2 for x in range(6)]
print('Squares:', squares)

# Example 6: Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Matrix Element [1][2]:', matrix[1][2])

# Example 7: Dictionary Basics
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print('Name:', person['name'])

# Example 8: Adding and Removing Dictionary Keys
person['profession'] = 'Engineer'
del person['age']
print('Updated Dictionary:', person)

# Example 9: Dictionary Methods
keys = list(person.keys())
values = list(person.values())
print('Keys:', keys)
print('Values:', values)

# Example 10: Tuples
coordinates = (10, 20)
print('X Coordinate:', coordinates[0])

# Example 11: Sets - Unique Elements
unique_numbers = set([1, 2, 2, 3, 4, 4, 5])
print('Unique Numbers:', unique_numbers)

# Example 12: Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print('Union:', set_a | set_b)
print('Intersection:', set_a & set_b)

# Example 13: String Formatting
name = 'John'
print(f'Hello, {name}! Welcome to Python.')

# Example 14: Multi-line Strings
message = """This is a multi-line
string in Python.
It supports multiple lines."""
print(message)

# Example 15: String Methods
text = 'hello world'
print('Uppercase:', text.upper())
print('Title Case:', text.title())

