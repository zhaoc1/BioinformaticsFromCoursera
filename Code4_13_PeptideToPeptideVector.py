#Chunyu Zhao
import sys

massTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, \
			'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, \
			'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, \
			'V': 99, 'Y': 163,'X':4,'Z':5}

def get_mass(peptide):
	if len(peptide) == 0:
		return 0
	return sum([massTable[pep] for pep in peptide])

def peptide_vector(peptide):
	mass = []
	for i in range(1,len(peptide)+1):
		mass.append(get_mass(peptide[:i]))
	pepVec = [0] * max(mass)
	for mi in mass:
		pepVec[mi-1] = 1
	return pepVec

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		peptide = lines[0]
	else:
		peptide = 'XZZXX'
	ret = peptide_vector(peptide)
	print ' '.join(map(str,ret))