OUT = {
    'A': [],
    'C': [],
    'G': [],
    'T': []
}

user_name = input()
d = {}

while user_name[0] != '':
    d[user_name] = ''
    DNA = input()
    if user_name != '>':
        while DNA[0] != '>':
            d[user_name] += DNA
            DNA = input()
        user_name = DNA
    else:
        break

print(d)
del d['>']

FASTA = []
for i in d:
    FASTA.append(d[i])

print(FASTA)

for i in range(len(FASTA[0])):
    OUT['A'].append(0)
    OUT['C'].append(0)
    OUT['G'].append(0)
    OUT['T'].append(0)

print(OUT)

for i in range(len(FASTA)):
    for j in range(len(FASTA[0])):
        if FASTA[i][j] == 'A':
            OUT['A'][j] += 1
        elif FASTA[i][j] == 'C':
            OUT['C'][j] += 1
        elif FASTA[i][j] == 'G':
            OUT['G'][j] += 1
        elif FASTA[i][j] == 'T':
            OUT['T'][j] += 1

print(OUT)

for i in range(len(FASTA[0])):
    if OUT['A'][i] == max(OUT['A'][i], OUT['C'][i], OUT['G'][i], OUT['T'][i]):
        print('A', end='')
    elif OUT['C'][i] == max(OUT['A'][i], OUT['C'][i], OUT['G'][i], OUT['T'][i]):
        print('C', end='')
    elif OUT['G'][i] == max(OUT['A'][i], OUT['C'][i], OUT['G'][i], OUT['T'][i]):
        print('G', end='')
    elif OUT['T'][i] == max(OUT['A'][i], OUT['C'][i], OUT['G'][i], OUT['T'][i]):
        print('T', end='')
print()

print('A:', end=' ')
for i in range(len(FASTA[0])):
    print(OUT['A'][i], end=' ')
print()

print('C:', end=' ')
for i in range(len(FASTA[0])):
    print(OUT['C'][i], end=' ')
print()

print('G:', end=' ')
for i in range(len(FASTA[0])):
    print(OUT['G'][i], end=' ')
print()

print('T:', end=' ')
for i in range(len(FASTA[0])):
    print(OUT['T'][i], end=' ')
print()
