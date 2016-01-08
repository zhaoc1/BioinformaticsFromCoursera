#Chunyu Zhao 20151122
import sys 

massTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, \
			'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, \
			'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, \
			'V': 99, 'Y': 163,'X':4,'Z':5}

def get_mass(peptide):
	if len(peptide) == 0:
		return 0
	return sum( massTable[pep] for pep in peptide )

def peptide_vector(peptide):
	mass = []
	for i in range(1,len(peptide)+1):
		mass.append(get_mass(peptide[:i]))
	pepVec = [0] * max(mass)
	for mi in mass:
		pepVec[mi-1] = 1
	return pepVec

def peptide_identification(proteome,specVec):
	massSpec = len(specVec)
	peptides = []
	for i in xrange(len(proteome)):
		for j in xrange(i+1,len(proteome)):
			masspep = get_mass(proteome[i:j])
			if masspep == massSpec:
				pepVec = peptide_vector(proteome[i:j])
				if len(pepVec) == len(specVec):
					peptides.append(proteome[i:j])
			elif masspep > massSpec:
				#if the prefix is already larger, then dont need to consider the rest
				break
	if len(peptides) != 0:
		maxScore = float('-inf')
		for peptide in peptides:
			pepVec = peptide_vector(peptide)
			score = sum([pepVec[i]*specVec[i] for i in xrange(len(pepVec))])
			if score > maxScore:
				maxScore = score
				pepHit = peptide
	else:
		pepHit = []
	return pepHit

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		specVec = map(int,lines[0].strip().split())
		proteome = lines[1]
	else:
		specVec = map(int,'0 0 0 4 -2 -3 -1 -7 6 5 3 2 1 9 3 -8 0 3 1 2 1 8'.split())
		proteome = 'XZZXZXXXZXZZXZXXZ'
		
	peptide = peptide_identification(proteome,specVec)
	

if __name__ == '__main__':
	main()
