# 6. Repeating work with a for loop
# range(1, 6) produces 1, 2, 3, 4, 5.

print("Counting from 1 to 5:")
for number in range(1, 6):
    print(number)

# A loop can also repeat a calculation.
table_number = int(input("Which multiplication table? "))
for number in range(1, 11):
    print(table_number, "x", number, "=", table_number * number)
