# File Creation
with open("my_file.txt", 'w') as file:
    file.write("Hello, this is line 1.\n")
    file.write("12345\n")
    file.write("This is line 3 with some numbers: 98765\n")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("Contents of my_file.txt:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied while trying to read the file.")
finally:
    file.close()

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("This is line 4 appended.\n")
        file.write("Another line with text.\n")
        file.write("Appending more numbers: 24680\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied while trying to append to the file.")
finally:
    file.close()
