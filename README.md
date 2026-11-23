# Python Basics – 10 Beginner Scripts

These examples are designed for a first introduction to Python. They use only Python's built-in features; no extra packages are needed.

## How to run
1. Install Python 3 from https://www.python.org/downloads/ if it is not already installed.
2. Open a terminal in this folder.
3. Run one script at a time, for example: `python 01_hello_world.py`.
   On some systems, use `python3` instead of `python`.
4. Try changing the code and run it again.

## Lesson guide

### 01_hello_world.py — Printing output
Introduces Python statements and print().
**Practice:** Change the messages and print your name.

### 02_variables_and_data_types.py — Variables and data types
Shows how to store text, whole numbers, decimal numbers, and True/False values. type() reports a value's type.
**Practice:** Create variables for your favourite subject and your exam score. Print them and their types.

### 03_user_input.py — User input
input() pauses the program and reads what the user types. int() converts numeric text into a whole number.
**Practice:** Ask for a favourite colour and birth year, then print both.

### 04_simple_calculator.py — Arithmetic
Demonstrates +, -, *, /, float(), and a check that prevents division by zero.
**Practice:** Add a remainder calculation using the % operator.

### 05_if_else_conditions.py — Conditions
if, elif, and else let a program choose what to do. Comparisons include >=, <, and !=.
**Practice:** Add a rule that prints 'Excellent' for marks of 95 or more.

### 06_for_loop.py — for loops
A for loop repeats a block. range(1, 6) starts at 1 and stops before 6.
**Practice:** Print the numbers from 10 down to 1 using range().

### 07_while_loop.py — while loops
A while loop repeats while its condition remains true. Updating count prevents an endless loop.
**Practice:** Change the loop so it counts from 1 to 10.

### 08_lists.py — Lists
Lists hold multiple items. Indexes start at zero; append() adds an item and len() counts items.
**Practice:** Add two more fruits and print the last item using a negative index.

### 09_functions.py — Functions
def creates a function. Parameters receive inputs, and return sends a result back to the caller.
**Practice:** Write a function called multiply() that returns the product of two numbers.

### 10_read_and_write_file.py — File handling
open() accesses a file. 'w' writes and 'r' reads. The with statement closes the file safely.
**Practice:** Add a third line to notes.txt, then run the program again and read it.

## Suggested teaching approach
- First, demonstrate the script without changing it.
- Ask students to predict what it will display.
- Run it and compare the result with their prediction.
- Change one line at a time and run it again.
- Let students complete the practice task independently.

## Important beginner ideas
- Python runs instructions from top to bottom, except where conditions, loops, and functions change the flow.
- Indentation matters: lines inside an `if`, loop, or function must be indented consistently.
- Text values need quotes; variable names do not.
- Read error messages carefully. They often point to the line that needs attention.