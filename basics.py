import sys
import os

# SYS MODULE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("\nSYS Module", "="*50)

print("\nVERSION", "-"*53)
print(sys.version)

print("\nARGV", "-"*56)
print(sys.argv)

print()

# OS MODULE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("\nOS Module", "="*51)

print("\nCWD", "-"*57)
print(os.getcwd())

os.chdir("../")
print("\nCWD", "-"*57)
print(os.getcwd())

"""
Other useful methods:

.remove("path of file") > removes a file
.mkdir("path where dir will be created") > makes a directory in the path
.rmdir("path of dir") > removes the dictionary
.path.join("path1", "path2") > path2 will be joined to path1

"""
print()
