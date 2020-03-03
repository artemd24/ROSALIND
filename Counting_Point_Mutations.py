first_DNA = input()
second_DNA = input()
intersections = 0

for i in range(len(first_DNA)):
    if first_DNA[i] != second_DNA[i]:
        intersections += 1

print(intersections)
