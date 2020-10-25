NAME_DNA = {}
CHILDRENS = {}
N = 3

# Read file
with open('rosalind_grph.txt', 'r') as file:
    lines = file.readlines()

# Fill NAME_DNA: key=DNA_STRING, value=STRING_NAME
for i in range(2, len(lines), 3):
    NAME_DNA[lines[i-1][:-1]+lines[i][:-1]] = lines[i-2][1:-1]

for key in NAME_DNA.keys():
    for dif_key in NAME_DNA.keys():
        if key != dif_key and key[(-1*N):] == dif_key[:N]:
            if NAME_DNA[key] not in CHILDRENS:
                CHILDRENS[NAME_DNA[key]] = [NAME_DNA[dif_key]]
            else:
                CHILDRENS[NAME_DNA[key]].append(NAME_DNA[dif_key])

for key in CHILDRENS.keys():
    for value in CHILDRENS[key]:
        print(key, value)
