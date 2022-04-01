# Max Clingroth
# CSC 120 Midterm Question 2
username = input("Enter a username: ")
if len(username) <= 6:
    print("Invalid username. The length should be greater than 6 characters")
elif not username.islower():
    print("Invalid username. Uppercase character found")
else:
    print("Valid username")
