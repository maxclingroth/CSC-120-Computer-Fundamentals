string = input("Enter a string: ").upper()
print()
frequency_dict = {}
for char in string:
    if "A" <= char <= "Z":
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
print("Dictionary:", frequency_dict)
letter = input("Enter a letter: ").upper()
# input validation
while letter <= "A" or letter >= "Z":
    print("Invalid character entered")
    letter = input("Enter a letter: ").upper()
if letter in frequency_dict:
    print("Frequency count of that letter:", frequency_dict[letter])
    del frequency_dict[letter]
    print("Dictionary after letter removed:", frequency_dict)
else:
    print("Letter not in dictionary")
letter_list = list(frequency_dict.keys())
letter_list.sort()
print("Letters sorted:", letter_list)
