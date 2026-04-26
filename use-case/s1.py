import os

folders = input("Please provide the list of directories with spaces:")
print(folders)
print(type(folders))
folders_split = folders.split()
print(folders_split)
print(type(folders_split))

for dir in folders_split:
    print(dir)
    try:
        files = os.listdir(dir)
        
    except FileNotFoundError:
        print("Please provide a valid dir ")
    else:
        print(files)

