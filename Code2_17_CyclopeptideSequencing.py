 
#Chunyu Zhao 20150912, 20150913 
import sys

def cycloPeptideSequencing(spectrum):
	'''only consider those Spectrum that appear in the spectrum'''
	TheoSpectrum = [128, 129, 131, 147, 101, 103, 137, 71, 99, 113, 114, 115, 97, 163, 87, 57, 186, 156]
	Spectrum = []
	for spec in TheoSpectrum:
		if spec in spectrum:
			Spectrum.append(spec)
	'''initialize'''
	peptides = [[0]]
	parentMass = max(spectrum)
	ret = []
	while len(peptides) != 0:
		''' expand the peptide '''
		newpeptides = []
		for peptide in peptides:
			for s in Spectrum:
				newpeptide = peptide + [s]
				if sum(newpeptide) == parentMass:
					if cyclicSpectrum(newpeptide[1:]) == spectrum:
						ret.append(newpeptide[1:])
				elif notconsistent(newpeptide,spectrum):
					continue
				else:
					newpeptides.append(newpeptide)
		peptides = newpeptides
	return ret

def notconsistent(peptide,specturm):
	''' every mass in its theoretical_spectrum must be contained in Spectrum'''
	if len([i for i,p in enumerate(peptide) if p not in spectrum]) > 0:
		return 1
	for p in peptide:
		if peptide.count(p) > spectrum.count(p):
			return 1
	''' for now we can only consider the linear spectrum'''
	theo = linearSpectrum(peptide[1:])
	for p in theo:
		if theo.count(p) > spectrum.count(p):
			return 1
	return 0

def linearSpectrum(peptide):
	prefixMass = [0]*(len(peptide)+1)
	for i in range(len(peptide)):
		prefixMass[i+1] = prefixMass[i] + peptide[i]
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
	if len(sys.argv) == 1:
		spectrum = [0,113,128,186,241,299,314,427]
	else:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		spectrum = map(int,lines[0].split(' '))
		
	peptides = cycloPeptideSequencing(spectrum)
	ret = []
	for pep in sorted(peptides):
		ret.append('-'.join(map(str,pep)))
	print ' '.join(ret)
