
def rna_to_protein(rna: str):
    bases = ['U', 'C', 'A', 'G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))
    SOLUTION = ''

    for i in range(2, len(rna), 3):
        if codon_table[rna[i-2] + rna[i - 1] + rna[i]] != '*':
            SOLUTION += codon_table[rna[i-2] + rna[i - 1] + rna[i]]
        else:
            break

    return SOLUTION


def dna_to_rna(dna: str):
    rna = ''
    for i in dna:
        if i == 'T':
            rna += 'U'
        else:
            rna += i
    return rna


NAME_DNA = []

# Read file
with open('rosalind_splc.txt', 'r') as file:
    lines = file.readlines()

# Fill NAME_DNA: key=DNA_STRING, value=STRING_NAME
for i in range(1, len(lines), 2):
    NAME_DNA.append(lines[i][:-1])

DNA = NAME_DNA[0]

for intron in NAME_DNA[1:]:
    DNA = DNA.replace(intron, '')

print(rna_to_protein(dna_to_rna(DNA)))
