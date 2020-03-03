# really cool code
RNA = input()

bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

for i in range(0, len(RNA), 3):
    if codon_table[RNA[i] + RNA[i+1] + RNA[i+2]] != '*':
        print(codon_table[RNA[i] + RNA[i+1] + RNA[i+2]], end='')
    else:
        break
