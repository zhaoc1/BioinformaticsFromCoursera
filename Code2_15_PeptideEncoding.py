"""
Protein Encoding Problem
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

def piptide_encoding(text,peptide):
       k = 3 * len(peptide)
       ret = []
       for i in range(len(text)-k+1):
              rna = text[i:i+k].replace('T','U')
              protein = rna_translate_protein(rna)
              if protein == peptide:
                     ret.append(text[i:i+k])
       reversetext = reverse_complement(text)
       for i in range(len(reversetext)-k+1):
              rna = reversetext[i:i+k].replace('T','U')
              protein = rna_translate_protein(rna)
              if protein == peptide:
                     ret.append(reverse_complement(reversetext[i:i+k]))
       return ret

def count_seq(peptide):
       ret = 1
       for pep in peptide:
              ret = ret * len([i for i, v in GeneticCode.items() if v == pep])
       print ret

def reverse_complement(dna):
       dnadict = {'A':'T','C':'G','G':'C','T':'A'}
       reverseDna = [ dnadict[c] for c in dna ]
       reverseDna = reverseDna[::-1]
       return ''.join(reverseDna)

if __name__ == '__main__':
       if len(sys.argv) == 2:
              filename = sys.argv[1]
              with open(filename) as f:
                     lines = f.read().splitlines()
              text = lines[0]
              peptide = lines[1]
       else:
              text = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
              peptide = "MA"
       protein = piptide_encoding(text,peptide)
       print '\n'.join(protein)
