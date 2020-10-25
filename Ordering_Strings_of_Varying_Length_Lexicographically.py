line = input().split()
N = int(input())

for i in line:
    for j in ([' '] + line):
        for p in ([' '] + line):
            if i != ' ' and not (j == ' ' and p != ' '):
                print(i + j + p)
