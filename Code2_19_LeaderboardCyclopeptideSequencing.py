"""
Leaderboard Cyclopeptide Sequencing Problem
"""
#Chunyu Zhao 20150921

import sys, collections

def leaderboardCyclopeptideSequencing(expSpectrum,N,theoSpectrum = [128, 129, 131, 147, 101, 103, 137, 71, 99, 113, 114, 115, 97, 163, 87, 57, 186, 156]):
	leaderboard = [[0]]
	leaderPeptide = [0]
	parentMass = max(expSpectrum)
	finalRet = {}
	while len(leaderboard) != 0:
		newleaderboard = []
		''' expand the leaderboard '''
		for peptide in leaderboard:
			for s in theoSpectrum:
				newpeptide = peptide + [s]
				if sum(newpeptide) == parentMass:
					leaderPeptideScore = cyclic_scoring(leaderPeptide,expSpectrum)
					newPeptideScore = cyclic_scoring(newpeptide[1:],expSpectrum)
					if newPeptideScore > leaderPeptideScore:
						leaderPeptide = newpeptide[1:]
					elif newPeptideScore == leaderPeptideScore:
						if newPeptideScore in finalRet:
							finalRet[newPeptideScore].append(newpeptide[1:])
						else:
							finalRet[newPeptideScore] = [newpeptide[1:]]
					newleaderboard.append(newpeptide)
				elif sum(newpeptide) > parentMass:
					continue
				else:
					newleaderboard.append(newpeptide)
		leaderboard = trim(newleaderboard,expSpectrum,N)
	return leaderPeptide,finalRet

def trim(leaderboard,expSpectrum,N):
	linearScores = [0] * len(leaderboard)
	for j in range(len(leaderboard)):
		peptide = leaderboard[j]
		linearScores[j] = cyclic_scoring(peptide,expSpectrum)
	''' sort X based on the value Y: [x for (y,x) in sorted(zip(Y,X),reverse=True)] '''
	leaderboardSorted = [x for (y,x) in sorted(zip(linearScores,leaderboard),reverse=True)]
	linearScoresSorted = sorted(linearScores,reverse=True)
	for j in range(N,len(leaderboardSorted)):
		if linearScoresSorted[j] < linearScoresSorted[N-1]:
			leaderboardSorted[j:] = []
			break
	return leaderboardSorted

def linear_scoring(peptide,expSpectrum):
	''' use the linear spectrum '''
	theoSpectrum = linearSpectrum(peptide)
	theoSpec_multiset = collections.Counter(theoSpectrum)
	expSpec_multiset = collections.Counter(expSpectrum)
	overlap = list((theoSpec_multiset & expSpec_multiset).elements())
	return len(overlap) 

def cyclic_scoring(peptide,expSpectrum):
	theoSpectrum = cyclicSpectrum(peptide)
	theoSpec_multiset = collections.Counter(theoSpectrum)
	expSpec_multiset = collections.Counter(expSpectrum)
	overlap = list((theoSpec_multiset & expSpec_multiset).elements())
	return len(overlap)

MassTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, \
			'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, \
			'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, \
			'V': 99, 'Y': 163}

def linearSpectrum(peptide):
	prefixMass = [0]*(len(peptide)+1)
	for i in range(len(peptide)):
		prefixMass[i+1] = prefixMass[i] + peptide[i]# ADD MassTable back# remove the MassTable when peptide are provided as integers.
	linearSpec = [0]
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			linearSpec.append(prefixMass[j]-prefixMass[i])
	return sorted(linearSpec)
def cyclicSpectrum(peptide):
	prefixMass = [0]*(len(peptide)+1)
	for i in range(len(peptide)):
		prefixMass[i+1] = prefixMass[i] + peptide[i]
	peptideMass = prefixMass[-1]
	cyclicSpec = [0]
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			cyclicSpec.append(prefixMass[j]-prefixMass[i])
			if i > 0 and j < len(peptide):
				cyclicSpec.append(peptideMass - prefixMass[j] + prefixMass[i]) #<--SUPER SMART
	return sorted(cyclicSpec)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		N = int(lines[0])
		expSpectrum = map(int,lines[1].split(' '))
	else:
		N = 10
		expSpectrum = [0,71,113,129,147,200,218,260,313,331,347,389,460]

	leadPeptide,leadBoard = leaderboardCyclopeptideSequencing(expSpectrum,N)
	print '-'.join(map(str,leadPeptide))
	