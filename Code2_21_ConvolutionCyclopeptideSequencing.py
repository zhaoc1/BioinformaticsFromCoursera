'''
Convotluion Cyclopeptide Sequencing Problem
'''
#Chunyu Zhao 20150922
import sys, Code2_19_LeaderboardCyclopeptideSequencing as cycloSeq
from collections import Counter

def spectral_convolution(spectrum):
	convolution = []
	spectrum = sorted(spectrum)
	for i in range(len(spectrum)):
		for j in range(i+1,len(spectrum)):
			if spectrum[j]-spectrum[i] >=57 and  spectrum[j]-spectrum[i] < 200:
				convolution.append(spectrum[j]-spectrum[i])
	return convolution 

def convolution_cyclopeptide_sequencing(spectrum,M,N):
	convolution = spectral_convolution(spectrum)
	theoSpecScore = [ c[1] for c in Counter(convolution).most_common(M)] #<-- DIDN'T CONSIDER TIES
	threshold = min(theoSpecScore)
	convolution = dict(Counter(convolution))
	theoSpec = [k for k,v in convolution.items() if v>=threshold]
	leadPeptide, leadBoard = cycloSeq.leaderboardCyclopeptideSequencing(spectrum,N,theoSpec)
	return leadPeptide,leadBoard

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		M = int(lines[0])
		N = int(lines[1])
		spectrum = map(int,lines[2].split(' '))
	else:
		M = 20
		N = 60
		spectrum = [57,57,71,99,129,137,170,186,194,208,228,265,285,299,307,323,356,364,394,422,493]

	leadPeptide,leadBoard = convolution_cyclopeptide_sequencing(spectrum,M,N)
	maxScore = max(leadBoard.keys())
	print ' '.join(['-'.join(map(str,l)) for l in leadBoard[maxScore]])