scores = input("Input a list of scores")

for n in range(0, len(scores)):
    scores[n] = int(scores[n])

highest = 0

for score in scores:
    if score > highest:
        highest = score
print(highest)