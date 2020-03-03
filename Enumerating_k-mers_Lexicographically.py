import itertools


symbols_connection = input().split()
k = int(input())

for i in itertools.product(symbols_connection, repeat=k):
    for j in range(k):
        print(i[j], end='')
    print()
