# Max Clingroth
# 2/1/2022
# CSC 120 Lab 4 Challenge Question 1
item_prices = [10, 40, 1, 16, 25, 34, 49, 40]
# i is the index of the first value being checked,
# j is the index of the second value, which checks
# each value from i to the end of the list except i itself
i = 0
j = 1
while i < len(item_prices):
    item1 = item_prices[i]
    while j < len(item_prices):
        item2 = item_prices[j]
        if item1 + item2 == 50:
            print(f"{item1}, {item2}")
        j += 1
    i += 1
    # Resets j and increments by 1
    j = i + 1
