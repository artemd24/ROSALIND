protein = input()
count_RNA = 1

amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i in protein:
    s = 0
    for j in amino_acids:
        if i == j:
            s += 1
    if s != 0:
        count_RNA *= s

print(count_RNA*3 % 1000000)
