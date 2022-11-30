heights = input("Input a list of students height").split()

for n in range(0, len(heights)):
    heights[n] = int(heights[n])


sum = 0
length = 0
for height in heights:
    sum += height
    length += 1

print(round(sum/length))