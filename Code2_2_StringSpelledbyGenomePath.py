"""
String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.
     Input: A sequence of k-mers Pattern1, ... ,Patternn such that the last k - 1 symbols of Patterni are
     	equal to the first k-1 symbols of Patterni+1 for 1 <= i <= n-1.
     Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni  (for 1 <= i <= n).
"""
#Chunyu Zhao 20150829

import sys

def genomePathString(kmers):
	k = len(kmers[0])
	text = [kmers[0]]
	for i in range(1,len(kmers)):
		text.append(kmers[i][k-1]) ## the [-1] of the last element is "\n", [k-1] is safer.
	text = ''.join(text)
	return text

if len(sys.argv) == 2:
	filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	kmers = lines
else:
	kmers = ['ACCGA','CCGAA','CGAAG','GAAGC','AAGCT']

genomeText = genomePathString(kmers)
print genomeText