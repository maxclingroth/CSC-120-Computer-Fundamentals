# Max Clingroth
# 2/1/2022
# CSC 120 Lab 4 Challenge Question 2
names = ["sarang", "john", "lily", "jasmine", "mara", "dave", "chester"]
name = input("Enter a name: ")
if name.lower() in names:
    print("Name found:", name)
else:
    print("Name not found")
