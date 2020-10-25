# really cool code
RNA = input()


def rna_to_protein(rna: str):
    bases = ['U', 'C', 'A', 'G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))
    SOLUTION = ''

    for i in range(0, len(rna), 3):
        if codon_table[rna[i] + rna[i + 1] + rna[i + 2]] != '*':
            SOLUTION += codon_table[rna[i] + rna[i + 1] + rna[i + 2]]
        else:
            break

    return SOLUTION


print(rna_to_protein(RNA))
