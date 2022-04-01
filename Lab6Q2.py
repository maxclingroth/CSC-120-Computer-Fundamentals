int_list = []
# loop with input validation
again = "y"
while again == "y":
    try:
        num = int(input("Enter an integer from 1 to 10: "))
        if 1 <= num <= 10:
            int_list.append(num)
            again = input("Enter another integer?[y/n] ").lower()
            while again != "y" and again != "n":
                print("Invalid input")
                again = input("Enter another integer?[y/n] ").lower()
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")
print("Number list:", int_list)
print("Largest element:", max(int_list))
print("Smallest element:", min(int_list))
total = sum(int_list)
length = len(int_list)
print("Sum of all elements:", total)
print("Length of list:", length)
print("Average:", total / length)
int_list.reverse()
print("List reversed:", int_list)
int_list.insert(0, int_list[-1])
int_list.pop()
print("Last element moved to front:", int_list)
