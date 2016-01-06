"""
Protein Translation Problem: Translate an RNA string into an amino acid string.
     Input: An RNA string Pattern and the array GeneticCode.
     Output: The translation of Pattern into an amino acid string Peptide.
"""
#Chunyu Zhao 20150913

import sys
GeneticCode = {'ACC': 'T', 'GCA': 'A', 'AAG': 'K', 'AAA': 'K', 'GUU': 'V', 'AAC': 'N', 'AGG': 'R', 'UGG': 'W', 'GUC': 'V', 'AGC': 'S', 'ACA': 'T', 'AGA': 'R', 'AAU': 'N', 'ACU': 'T', 'GUG': 'V', 'CAC': 'H', 'ACG': 'T', 'AGU': 'S', 'CCA': 'P', 'CAA': 'Q', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'CGA': 'R', 'CAG': 'Q', 'CGC': 'R', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'CCU': 'P', 'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'CCG': 'P', 'UCC': 'S', 'UAC': 'Y', 'CGU': 'R', 'GAA': 'E', 'AUA': 'I', 'AUC': 'I', 'CUU': 'L', 'UCA': 'S', 'AUG': 'M', 'UGA': '', 'CUG': 'L', 'GAG': 'E', 'AUU': 'I', 'CAU': 'H', 'CUA': 'L', 'UAA': '', 'GCC': 'A', 'UUU': 'F', 'GAC': 'D', 'GUA': 'V', 'UGC': 'C', 'GCU': 'A', 'UAG': '', 'CUC': 'L', 'UUG': 'L', 'UUA': 'L', 'GAU': 'D', 'UUC': 'F'}

def rna_translate_protein(rna):
       i = 0
       protein = []
       while i < len(rna)-2:
              if len(GeneticCode[rna[i:i+3]]) ==0:
                     return protein
              else:
                     protein.append(GeneticCode[rna[i:i+3]])
              i = i + 3
       return ''.join(protein)

   
if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		rna = lines[0]
	else:
		rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"""
	protein = rna_translate_protein(rna)
	print ''.join(protein)
