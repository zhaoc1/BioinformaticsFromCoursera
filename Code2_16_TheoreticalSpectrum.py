"""
Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
     Input: An amino acid string Peptide.
     Output: Cyclospectrum(Peptide).
"""
#Chunyu Zhao 20150912

import sys

MassTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, \
			'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, \
			'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, \
			'V': 99, 'Y': 163}

def theoretical_spectrum(peptide):
	k = len(peptide)
	spec = []
	while k > 0:
		for i in range(len(peptide)-k+1):
			subpep = peptide[i:i+k]
			spec.append(sum([MassTable[s] for s in subpep]))
		k -= 1
	spec.append(0)
	return sorted(spec)

def linearSpectrum(peptide):
	prefixMass = [0]*(len(peptide)+1)
	for i in range(len(peptide)):
		prefixMass[i+1] = prefixMass[i] + MassTable[peptide[i]]
	linearSpec = [0]
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			linearSpec.append(prefixMass[j]-prefixMass[i])
	return sorted(linearSpec)

def cyclicSpectrum(peptide):
	prefixMass = [0]*(len(peptide)+1)
	for i in range(len(peptide)):
		prefixMass[i+1] = prefixMass[i] + MassTable[peptide[i]]
	peptideMass = prefixMass[-1]
	cyclicSpec = [0]
	for i in range(len(peptide)):
		for j in range(i+1,len(peptide)+1):
			cyclicSpec.append(prefixMass[j]-prefixMass[i])
			if i > 0 and j < len(peptide):
				cyclicSpec.append(peptideMass - prefixMass[j] + prefixMass[i]) #<--Nice!
	return sorted(cyclicSpec)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		peptide = lines[0]
	else:
		peptide = 'NQEL'
	
	spec = cyclicSpectrum(peptide)
	print ' '.join(map(str,spec))
