# 5. Making decisions with if / elif / else
# Python runs a block depending on whether a condition is true.

marks = int(input("Enter your marks (0 to 100): "))

if marks < 0 or marks > 100:
    print("Please enter marks between 0 and 100.")
elif marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Needs improvement")
