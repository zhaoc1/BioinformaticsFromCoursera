#Chunyu Zhao 20151121
from collections import defaultdict
from itertools import imap
from operator import ne
from string import maketrans

# I refer to some online resources for learning some new Python skills
''' some really advanced data structures...very very good'''
def reverse_complement(dna):
	transtab = maketrans('ATCG','TAGC')
	return dna.translate(transtab)[::-1]

def shared_kmers(k,dna1,dna2):
	dna1Dict = defaultdict(list)
	for i in xrange(len(dna1)-k+1):
		dna1Dict[dna1[i:i+k]].append(i)
	return { (i,j) for j in xrange(len(dna2)-k+1) for i in dna1Dict[dna2[j:j+k]]+dna1Dict[reverse_complement(dna2[j:j+k])] }

def main():
	with open('dataset_289_5.txt') as input_data:
		k = int(input_data.readline().strip())
		dna1,dna2 = [line.strip() for line in input_data.readlines()]

	k = 3
	dna1 = 'TCAGTTGGCCTACAT'
	dna2 = 'CCTACATGAGGTCTG'
	shared_kmer_indices = map(str, sorted(shared_kmers(k, dna1, dna2)))

	print len(shared_kmer_indices)
	
	with open('result.txt', 'w') as output_data:
		output_data.write('\n'.join(shared_kmer_indices))

if __name__ == '__main__':
	main()