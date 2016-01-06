#Chunyu Zhao 20150923

import sys,random
from random import randint
from Code1_16_RandomizedMotifSearch import profileMatrixPesudocounts,profile_most_probable_kmer

def gibbsSampler(dnas,k,t,N):
	motifs = []
	for dna in dnas:
		istart = randint(0,len(dna)-k)
		motifs.append(dna[istart:istart+k])
	bestMotifs = motifs

	for j in range(N):
		
		r = randint(0,t-1)
		current_profile = profileMatrixPesudocounts([motif for index, motif in enumerate(motifs) if index!=r])
		motifs = [profile_most_probable_kmer(dnas[index],k,current_profile) if index == r else motif for index,motif in enumerate(motifs)]
		'''
		r = randint(0,t-1)
		profile = profileMatrixPesudocounts([motif for i,motif in enumerate(motifs) if i !=r ])
		randkmer = profile_random_kmer(dnas[r],profile)
		motifs[r] = randkmer
		'''
		if score(motifs) < score(bestMotifs):
			bestMotifs = motifs
	return bestMotifs

def profile_random_kmer(text,profile):
	nuc_loc = {nuc:i for i,nuc in enumerate('ACGT')}
	k = len(profile)
	probs = []
	for i in range(len(text)-k+1):
		prob = [profile[j][nuc_loc[nuc]] for j, nuc in enumerate(text[i:i+k]) ]
		probs.append(reduce(lambda x, y: x*y, prob))
	probs = [ float(prob)/float(sum(probs)) for prob in probs ] 
	irand = Random(probs)
	return text[irand:irand+k]

def Random(prob):
	totals = [ sum(prob[:i+1]) for i in range(len(prob)) ]
	randval = random.uniform(0,totals[-1])
	for i,v in enumerate(totals):
		if randval <= v:
			return i

def score(motifs):
	columns = [''.join(seq) for seq in zip(*motifs)]
	max_count = sum([ max([col.count(nuc) for nuc in 'ACGT']) for col in columns ])
	return len(motifs[0])*len(motifs) - max_count

if __name__ =='__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		k,t,N = map(int,lines[0].split(' '))
		dnas = lines[1:]
		#ol = [i for i,l in enumerate(lines) if l =='Output']
		#ol=ol[0]
		#dnas = lines[2:ol]
		''' LEARN FROM SOMEONE ELSE CODE'''
		#k,t = map(int, input_data.readline().split())
		#dna_list = [line.strip() for line in input_data.readlines()]
	else:
		k = 8
		t = 5
		N = 100
		dnas = ['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',\
		'TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',\
		'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

	bestScore = k*t
	bestMotif = None
	for repeat in xrange(1000):
		motifs = gibbsSampler(dnas,k,t,N)
		if score(motifs) < bestScore:
			bestMotif = motifs
			bestScore = score(bestMotif)
	print '\n'.join(bestMotif)