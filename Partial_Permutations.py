n, k = map(int, input().split())

permutations_number = 1
for i in range(n-k+1, n+1):
    permutations_number *= i

print(permutations_number % 1000000)
