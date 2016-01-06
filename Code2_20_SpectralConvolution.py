#Chunyu Zhao 20150921
import sys

def spectral_convolution(spectrum):
	convolution = []
	spectrum = sorted(spectrum)
	for i in range(len(spectrum)):
		for j in range(i+1,len(spectrum)):
			if spectrum[j]-spectrum[i] > 0 :
				convolution.append(spectrum[j]-spectrum[i])
	return convolution

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		spectrum = map(int,lines[0].split(' '))
	else:
		spectrum = [0,137,186,323]

	convolution = spectral_convolution(spectrum)
	print ' '.join(map(str,convolution))
