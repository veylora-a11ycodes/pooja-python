import os

directory_path = os.path.dirname(os.path.abspath(__file__))

contents = os.listdir(directory_path)

for item in contents:
    print(item)
