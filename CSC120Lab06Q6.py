# Max Clingroth
# Lab 06 Question 6
SCORES = [40,91,85,15]
i = 0
while i < len(SCORES):
    j = i + 1
    while j < len(SCORES):
        print(SCORES[i], SCORES[j])
        j += 1
    i += 1
