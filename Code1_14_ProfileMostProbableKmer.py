#Chunyu Zhao 20150915

import sys

def profileMostProbableKmer(text,k,profile):
	xaxis = {'A':0,'C':1,'G':2,'T':3}
	maxprob = float('-inf')
	maxkmer = None
	for i in range(len(text)-k+1):
		kmer = text[i:i+k]
		prob = 1
		for ki in range(len(kmer)):
			prob = prob * profile[xaxis[kmer[ki]]][ki]
		if prob > maxprob:
			maxkmer = kmer
			maxprob = prob
	return maxkmer

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]
		k = int(lines[1])
		profile = [map(float,l.split(' '))for l in lines[2:]]

	kmers = profileMostProbableKmer(text,k,profile)
	print kmers