# 1. Print Statements:
name = "shahzad"
age = 28

print("Hello, my name is", name, "and I am", age, "years old.")
print(f"Hello, my name is {name} and I am {age} years old.")


# 2. Strings:
texting = "Hello, My Dear Sir Zia Khan!"
print(texting.upper())  # Output: HELLO, WORLD!
print(texting.lower())  # Output: hello, world!
print(texting.replace("world", "there"))  # Output: Hello, there!


# 3. f-Strings:

name = "Muhammad Shahzad"
age = 35

print(f"Hello, my name is {name} and I am {age} years old.")
# 4. Operators:
x = 7
y = 4

print(x + y)  # Output: 11
print(x - y)  # Output: 3
print(x * y)  # Output: 28
print(x / y)  # Output: 1.75
print(x % y)  # Output: 3
print(x ** y)  # Output: 2401

# 5. Lists:

fruits = ["grape", "mango", "cherry"]
print(fruits[0])  # Output: grape
fruits.append("orange")
print(fruits)  # Output: ['grape', 'mango', 'cherry', 'orange']
fruits.remove("mango")
print(fruits)  # Output: ['grape', 'cherry', 'orange']

# 6. Tuples:

numbers = (5, 19, 40)
print(numbers[0])  # Output: 5
#numbers[0] = 5  # This will raise an error as tuples are immutable

# 7. For Loops:

for i in range(6):
    print(i)  # Output: 0 1 2 3 4 5

numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number)  # Output: 1 2 3 4 5 6


# 8. Input Handling:

name = input("Enter your name: ")
print("Hello, " + name + "!")
