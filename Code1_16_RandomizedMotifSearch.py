#Chunyun Zhao 20150923

import sys
from random import randint

def randomizedMotifSearch(dnas,k,t):
	motifs = []
	for dna in dnas:
		istart = randint(0,len(dna)-k)
		motifs.append(dna[istart:istart+k])

	bestMotifs = motifs

	while True:
		profile = profileMatrixPesudocounts(motifs)
		motifs = [profile_most_probable_kmer(dna,k,profile) for dna in dnas]
		if score(motifs) < score(bestMotifs):
			bestMotifs = motifs
		else:
			return bestMotifs

def profileMatrixPesudocounts(motifs):
	columns = [''.join(seq) for seq in zip(*motifs)]
	profile = [ [float(col.count(nuc)+1) / float(len(col)+4) for nuc in 'ACGT'] for col in columns]
	return profile

def profile_most_probable_kmer(text,k,profile):
	xaxis = {'A':0,'C':1,'G':2,'T':3}
	maxprob = float('-inf')
	maxkmer = None
	for i in range(len(text)-k+1):
		kmer = text[i:i+k]
		prob = 1
		for ki in range(len(kmer)):
			prob = prob * profile[ki][xaxis[kmer[ki]]]
		if prob > maxprob:
			maxkmer = kmer
			maxprob = prob
	return maxkmer

def hamming_distance(str1,str2):
	hd = 0
	if len(str1) != len(str2):
		print "the two strings different length ERROR"
		return None
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			hd += 1
	return hd

def score(motifs):
	columns = [''.join(seq) for seq in zip(*motifs)]
	max_count = sum([ max([col.count(nuc) for nuc in 'ACGT']) for col in columns ])
	return len(motifs[0])*len(motifs) - max_count


if __name__ =='__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		k,t = map(int,lines[0].split(' '))
		dnas = lines[1:]
		''' LEARN FROM SOMEONE ELSE CODE'''
		#k,t = map(int, input_data.readline().split())
		#dna_list = [line.strip() for line in input_data.readlines()]
	else:
		k = 8
		t = 5
		dnas = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',\
		'TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',\
		'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

	bestScore = k*t
	bestMotif = None
	for repeat in xrange(1000):
		motifs = randomizedMotifSearch(dnas,k,t)
		if score(motifs) < bestScore:
			bestMotif = motifs
			bestScore = score(bestMotif)
	print '\n'.join(bestMotif)
