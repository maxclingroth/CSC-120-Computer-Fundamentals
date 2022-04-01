# Max Clingroth
# CSC 120 Midterm Question 1
bitString = input("Enter a series of bits: ")

# input validation
while True:
    binary = True
    for bit in bitString:
        if bit != "0" and bit != "1":
            binary = False
    if binary:
        break
    else:
        print("Invalid entry")
        bitString = input("Enter a series of bits: ")

print("Most Significant Bit:", bitString[0])
