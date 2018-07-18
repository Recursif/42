

import os 

print("Path at terminal whn executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to as.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --->' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))

dirname, filename = os.path.split(os.path.abspath(__file__))

print(dirname)
print(filename)
