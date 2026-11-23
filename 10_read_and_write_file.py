# 10. Reading from and writing to a text file
# This program creates a file named notes.txt in the same folder.

# Write text to a file. "w" means write (it replaces old contents).
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python is fun to learn.\n")
    file.write("I am practising file handling.\n")

# Read the file and display its contents.
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()

print("Contents of notes.txt:")
print(contents)
