import itertools
import math

permutations = []
n = int(input())

for i in range(1, n + 1):
    permutations.append(i)
print(math.factorial(n))
for i in itertools.permutations(permutations):
    for j in range(n):
        print(i[j], end=' ')
    print()
