# 1. Print Statements:
name = "shahzad"
age = 35

print("Hello, my name is", name, "and I am", age, "years old.")
print(f"Hello, my name is {name} and I am {age} years old.")


# 2. Strings:

text = "Hello, world!"
print(text.upper())  # Output: HELLO, WORLD!
print(text.lower())  # Output: hello, world!
print(text.replace("world", "there"))  # Output: Hello, there!

# 3. f-Strings:

pi = 3.14159
radius = 5

area = pi * radius**2
print(f"The area of a circle with radius {radius} is {area:.2f}")  # Output: The area of a circle with radius 5 is 78.54

# 4. Operators:

x = 5
y = 3

print(x + y)  # Output: 8
print(x - y)  # Output: 2
print(x * y)  # Output: 15
print(x / y)  # Output: 1.6666666666666667
print(x % y)  # Output: 2
print(x ** y)  # Output:  

# 5. Lists:

fruits = ["apple", "banana", "orange"]
print(fruits[0])  # Output: apple
fruits.append("grape")
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'orange', 'grape']


# 6. Tuples:

coordinates = (10, 20)
print(coordinates[0])  # Output: 10
# coordinates[0] = 5  # This will raise an error as tuples are immutable


# 7. For Loops:

for i in range(5):
    print(i)  # Output: 0 1 2 3 4

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)  # Output: 1 2 3 4 5


# 8. Input Handling:

name = input("Enter your name: ")
print("Hello, " + name + "!")
