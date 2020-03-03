n, m = map(int, input().split())
MORTAL_FIB = [1, 1]

for i in range(2, n + 1):
    if i < m:
        MORTAL_FIB.append(MORTAL_FIB[i - 1] + MORTAL_FIB[i - 2])
    elif i == m:
        MORTAL_FIB.append(MORTAL_FIB[i - 1] + MORTAL_FIB[i - 2] - 1)
    else:
        MORTAL_FIB.append(MORTAL_FIB[i-1] + MORTAL_FIB[i-2] - MORTAL_FIB[i-m-1])

print(MORTAL_FIB[n-1])
