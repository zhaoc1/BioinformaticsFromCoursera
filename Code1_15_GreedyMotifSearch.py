#Chunyu Zhao 20150915
#! /usr/bin/env python
'''
Motif: a collection of k-mers taken from t strings DNA
Profile(motif): ~ four-sided biased die
'''
import sys,numpy as np

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

def greedyMotifSearch(dnas,k,t):
	''' run the greddy motif search algorithm and return the best motif '''
	bestMotifs = [dna[:k] for dna in dnas ]
	firstStrand = dnas[0]
	otherStrand = dnas[1:]
	for i in range(len(firstStrand)-k+1):
		motifs = [firstStrand[i:i+k]]
		for strand in otherStrand:
			profile = profileMatrixPesudocounts(motifs)
			motifs.append(profile_most_probable_kmer(strand,k,profile))
		if score(motifs) < score(bestMotifs):
			bestMotifs = motifs
	return bestMotifs

def score(motifs):
	'''i didn't think of this by myself... zan! 
	https://github.com/jschendel/Rosalind/blob/master/Textbook_03D.py'''
	columns = [''.join(seq) for seq in zip(*motifs)]
	max_count = sum([ max([col.count(nuc) for nuc in 'ACGT']) for col in columns ])
	return len(motifs[0])*len(motifs) - max_count

def profileMatrix(motifs):
	''' zip in conjunction with the * operator can be used to unzip a list '''
	columns = [''.join(seq) for seq in zip(*motifs)]
	profile = [ [float(col.count(nuc)) / float(len(col)) for nuc in 'ACGT'] for col in columns]
	return 

def profileMatrixPesudocounts(motifs):
	''' zip in conjunction with the * operator can be used to unzip a list '''
	columns = [''.join(seq) for seq in zip(*motifs)]
	profile = [ [float(col.count(nuc)+1) / float(len(col)*2) for nuc in 'ACGT'] for col in columns]
	return profile

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		k = int(lines[0].split(' ')[0])
		t = int(lines[0].split(' ')[1])
		dnas = lines[1:]
	else:	
		k = 3
		t = 5
		dnas = ['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG']
	motifs = greedyMotifSearch(dnas,k,t)
	print '\n'.join(motifs)

if __name__ == '__main__':
	main()