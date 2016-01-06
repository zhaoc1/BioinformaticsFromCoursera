"""
Implanted Motif Problem:
Find all (k, d)-motifs in a collection of strings. A collection of strings Dna, and integers k and d.
All (k, d)-motifs in Dna.
"""
#Chunyu Zhao
import sys

def hamming_distance(str1,str2):
	hd = 0
	if len(str1) != len(str2):
		print "the two strings different length ERROR"
		return None
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			hd += 1
	return hd

def neighbors(pattern,d):
	if d == 0:
		return pattern
	if len(pattern) == 1:
		return ['A','C','G','T']
	neighborhood = []
	suffixNeighbors = neighbors(pattern[1:],d)
	for text in suffixNeighbors:
		if hamming_distance(pattern[1:],text) < d:
			for x in ['A','C','G','T']:
				neighborhood.append(x+text)
		else:
			neighborhood.append(pattern[:1]+text)
	neighborhood = list(set(neighborhood))
	return neighborhood 

def motifEnumeration(dnas,k,d):
	''' enumerate all k-mers in collection of strings dnas '''
	patterns = []
	neighborhood = []
	for dna in dnas:
		temp = []
		neigh = []
		for i in range(len(dna)-k+1):
			temp.append(dna[i:i+k])
			neigh = neigh + neighbors(dna[i:i+k],d)
		neighborhood.append(temp + neigh)
		patterns = patterns + temp
	patterns = list(set(patterns))
	''' for each neighbors in each pattern '''
	motifs = []
	for pattern in patterns:
		kmers = neighbors(pattern,d)
		for kmer in kmers:
			locs = [i for i,dkmer in enumerate(neighborhood) if kmer in dkmer]
			if len(locs) == len(dnas):
				motifs.append(kmer)
	''' remove duplicates '''
	motifs = list(set(motifs))
	return motifs

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		k = int(lines[0].split(' ')[0])
		d = int(lines[0].split(' ')[1])
		dnas = lines[1:]
	else:
		dnas = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
		k = 3
		d = 1

	motifs = motifEnumeration(dnas,k,d)
	print ' '.join(sorted(motifs)) 