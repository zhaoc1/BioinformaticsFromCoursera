#Chunyu Zhao 20150921 

import sys,collections,Code2_16_TheoreticalSpectrum as ts

def cyclic_scoring(peptide,expSpectrum):
	theoSpectrum = ts.cyclicSpectrum(peptide)
	theoSpec_multiset = collections.Counter(theoSpectrum)
	expSpec_multiset = collections.Counter(expSpectrum)
	overlap = list((theoSpec_multiset & expSpec_multiset).elements())
	theoSpec_remainder = list((theoSpec_multiset - expSpec_multiset).elements())
	expSpect_remainder = list((expSpec_multiset - theoSpec_multiset).elements())
	return len(overlap)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		peptide = lines[0]
		expSpectrum = map(int,lines[1].split(' '))
	else:
		peptide = 'NQEL' 
		expSpectrum = [0,99,113,114,128,227,257,299,355,356,370,371,484]

	score = cyclic_scoring(peptide,expSpectrum)
	print score