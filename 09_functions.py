# 9. Creating and using functions
# A function is a reusable block of code.

def greet(person_name):
    print("Hello,", person_name)

def add(number1, number2):
    return number1 + number2

greet("Meera")
greet("Kabir")

answer = add(10, 20)
print("10 + 20 =", answer)
