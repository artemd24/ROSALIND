n, k = map(int, input().split())

FIB = [1, 1]
for i in range(2, n + 1):
    FIB.append(FIB[i-1] + (FIB[i-2])*k)

print(FIB[n-1])
