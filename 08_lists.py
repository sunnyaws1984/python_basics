# 8. Working with lists
# A list stores multiple values in one variable.
# List positions (indexes) start at 0.

fruits = ["apple", "banana", "mango"]

print("All fruits:", fruits)
print("First fruit:", fruits[0])

fruits.append("orange")  # Add an item
print("After adding orange:", fruits)

print("Fruit names one by one:")
for fruit in fruits:
    print(fruit)

print("Number of fruits:", len(fruits))
