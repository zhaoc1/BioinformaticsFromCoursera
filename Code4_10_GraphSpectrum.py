
#Chunyu Zhao 20151111
import sys

massTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, \
			'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, \
			'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, \
			'V': 99, 'Y': 163}

def spectrum_graph(Spectrum):
	Spectrum = sorted(Spectrum)
	for i in range(len(Spectrum)):
		for j in range(i+1,len(Spectrum)):
			if Spectrum[j]-Spectrum[i] in massTable.values():
				aa = [ key for key,val in massTable.items() if val == Spectrum[j]-Spectrum[i]]
				print str(Spectrum[i])+'->'+str(Spectrum[j]) + ':' + aa[0]

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		Spectrum = map(int,lines[0].split(' '))
	else:
		Spectrum = [57,71,154,185,301,332,415,429,486]
	
	Spectrum = [0] + Spectrum
	spectrum_graph(Spectrum)