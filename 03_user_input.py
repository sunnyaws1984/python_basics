# 3. Getting information from the user
# input() reads text typed by the user.

name = input("What is your name? ").strip()
city = input("Which city do you live in? ").strip()

# f-strings: f"Hello {name}!" puts the variable straight into the text.

print(f"Hello {name}!")
print(f"You live in {city}")

# input() returns text. Convert it to int when doing calculations.
age_text = input("How old are you? ").strip()

if age_text.isdigit():
    age = int(age_text)
    print(f"Next year you will be {age + 1}")
else:
    print("Please enter your age as a whole number.")