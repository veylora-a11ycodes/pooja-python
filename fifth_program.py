#label the program written in problem with comments

import os  # Import the os module

# Get the current file's directory path
folder = os.path.dirname(os.path.abspath(__file__))

# Print the folder location
print("Folder location:", folder)

# Get all files and folders from the directory
contents = os.listdir(folder)

# Print the contents of the directory
print("Files inside folder:")

# Print each file and folder separately
for item in contents:
    print(item)
