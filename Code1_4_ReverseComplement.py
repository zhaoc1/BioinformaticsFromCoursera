"""
Reverse Complement Problem: Find the reverse complement of a DNA string.
     Input: A DNA string Pattern.
     Output: Pattern, the reverse complement of Pattern.
"""
#Chunyu Zhao 20150904

import sys

def reverse_complement(dna):
	dnadict = {'A':'T','C':'G','G':'C','T':'A'}
	reverseDna = [ dnadict[c] for c in dna ]
	return reverseDna[::-1]

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		dna = lines[0]
	else:
		dna = 'AAAACCCGGT'

	reverseDNA = reverse_complement(dna)
	print ''.join(reverseDNA)
