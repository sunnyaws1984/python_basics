
# --------------------------------
# 1. SETS IN PYTHON
# --------------------------------

print("----- SET EXAMPLE -----")

# Creating a set
fruits = {"Apple", "Banana", "Mango", "Apple"}

# Display the set
print("Fruits:", fruits)

# Add an item
fruits.add("Orange")
print("After adding Orange:", fruits)

# Remove an item
fruits.remove("Banana")
print("After removing Banana:", fruits)

# Check if an item exists
print("Is Apple available?", "Apple" in fruits)


# --------------------------------
# 2. TUPLES IN PYTHON
# --------------------------------

print("\n----- TUPLE EXAMPLE -----")

# Creating a tuple
students = ("Rahul", "Priya", "Amit", "Sneha")

print("Original tuple:", students)

# Access first student
print("First student:", students[0])

# Trying to modify the first student
students[0] = "Rohit"

print("Updated tuple:", students)

