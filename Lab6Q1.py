first_scores = []
# loop that tests all inputs
i = 0
while i < 5:
    try:
        score = int(input("Enter a test score: "))
        if 0 <= score <= 100:
            first_scores.append(score)
            i += 1
        else:
            print("Invalid score entered")
    except ValueError:
        print("Invalid score entered")
print("All scores:",  first_scores)
print("Students who scored below a 60 get 10 extra points.")
second_scores = []
for score in first_scores:
    if score < 60:
        second_scores.append(score + 10)
    else:
        second_scores.append(score)
print("All scores:", second_scores)
print("Students whose scores have changed:")
for i in range(len(second_scores)):
    if second_scores[i] != first_scores[i]:
        print(f"Old score: {first_scores[i]} New score: {second_scores[i]}")
