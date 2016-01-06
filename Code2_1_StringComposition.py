"""
CODE CHALLENGE: Solve the String Composition Problem.
     Input: An integer k and a string Text.
     Output: Compositionk(Text) (the k-mers can be provided in any order).
"""
#Chunyu Zhao 20150829

import sys

def string_com(k,text):
	kmers = []
	for c in range(len(text)-k+1):
		kmers.append(text[c:c+k])
	kmers = sorted(kmers)
	return kmers

if len(sys.argv) == 2:
	filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	k = int(lines[0])
	text = lines[1]
else:
	k = 5
	text = 'CAATCCAAC'

kmers = string_com(k,text)
print "\n".join(kmers)
