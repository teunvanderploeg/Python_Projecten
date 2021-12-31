import os

files_deleted = 0
files = 0

print('=========================')
print('Files with specific extension deleter tool.')
print(os.getcwd())
print('=========================')

path = input("Path to files: ")
extension = input("File extension like [.jpg .pdf .txt]: ")

print(path + ' ' + extension)

for parent, dirnames, filenames in os.walk(str(path)):
    for filename in filenames:
        files = files + 1
        if filename.lower().endswith(str(extension)):
            os.remove(os.path.join(parent, filename))
            files_deleted = files_deleted + 1

print("Files: " + str(files))
print("Files deleted: " + str(files_deleted))
