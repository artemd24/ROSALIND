import itertools
from collections import Counter

n = int(input())
permutations = []
count = []

for i in range(1, n + 1):
    permutations.append(-i)
    permutations.append(i)

for i in itertools.permutations(permutations, n):
    test = []
    SUM = 0
    print(i)
    for j in range(n):
        test.append(abs(i[j]))
    print(test)
    c_test = Counter(test)
    for q in c_test:
        print(c_test[q])
        if c_test[q] >= 2:
            continue
        else:
            SUM += 1
        if SUM == n:
            count.append(i)

f = open('text.txt', 'w')
f.write(str(len(count)))
f.write('\n')
for i in count:
    for j in i:
        f.write(str(j) + ' ')
    f.write('\n')
