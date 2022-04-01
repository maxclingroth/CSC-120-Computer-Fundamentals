# Max Clingroth
# Lab 06 Extra Credit
def find_unique(s):
    letter_dict = {}
    for char in s:
        if char not in letter_dict:
            letter_dict[char] = True
        else:
            letter_dict[char] = False
    for char, unique in letter_dict.items():
        if unique:
            print(char, end=' ')


s = "i_love_programming_in_python_and_i_will_alzways_program"
find_unique(s)
