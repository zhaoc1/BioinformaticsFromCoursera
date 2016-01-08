#Chunyu Zhao 20151122
import sys

massTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, \
			'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, \
			'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, \
			'V': 99, 'Y': 163}

#massTable = {'X':4,'Z':5}

def get_size_spectral_dictionary(spectrum,threshold,maxscore):
	size = []
	for t in xrange(maxscore+1):
		size.append([0]*(len(spectrum)))
	size[0][0] = 1

	for i in range(1,len(spectrum)):
		for t in range(maxscore+1):
			total = 0
			for aa in massTable.keys():
				m = massTable[aa]
				if i-m>=0 and t-spectrum[i]<=maxscore and t-spectrum[i]>=0:
					total = total + size[t-spectrum[i]][i-m]
			size[t][i] = float(total)/20 # divided by 20 means 
	ret = 0
	for i in range(len(spectrum)-1,len(spectrum)):
		for t in range(maxscore+1):
			if t >= threshold and t<=maxscore:
				ret += size[t][i]
	return ret
	
def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		spectrum = lines[0]
		threshold = int(lines[1])
		maxscore = int(lines[2])
	else:
		spectrum = '4 -3 -2 3 3 -4 5 -3 -1 -1 3 4 1 3'
		threshold = 1
		maxscore = 8

	spectrum = map(int,[0] + spectrum.split(' '))
	specSize = get_size_spectral_dictionary(spectrum,threshold,maxscore)
	print specSize

if __name__ == '__main__':
	main()