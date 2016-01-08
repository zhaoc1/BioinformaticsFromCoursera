#Chunyu Zhao 
import sys, Code4_11_DecodeIdealSpectrum as decode

massTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, \
			'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, \
			'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, \
			'V': 99, 'Y': 163,'X':4,'Z':5}

def from_peptide_vector(vector):
	mass = [i+1 for i in range(len(vector)) if vector[i]==1]
	mass = [0] + mass
	return mass

def ideal_spectrum(peptide):
	idealPrefixSpec = []
	for i in range(1,len(peptide)+1):
		idealPrefixSpec.append(decode.get_mass(peptide[:i]))
	return idealPrefixSpec

def decode_ideal_spec(spec):
	specGraph,weighGraph = decode.spectrum_graph(spec)
	source = min(spec)
	sink = max(spec)
	edgeTo, marked,postorder = decode.depthFirstPaths(specGraph,source)
	paths,peptides = decode.pathTo(specGraph,weighGraph,source,sink,edgeTo)
	peptide = []
	for i in range(len(paths)-1):
		peptide.append(weighGraph[paths[i]][specGraph[paths[i]].index(paths[i+1])])
	return ''.join(peptide)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		pepvector = map(int,lines[0].split(' '))
	else:
		pepvector = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
	spec = from_peptide_vector(pepvector)
	print decode_ideal_spec(spec)

