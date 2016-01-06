#Chunyu Zhao 20150904

import sys, Code1_3_FasterFrequentWords as freqArray

def clumpfinding(genome,k,t,L):
	frequentPatterns = []
	clump = [0] * (4**k)
	for i in range(len(genome) - L + 1):
		text = genome[i:i+L]
		frequencyArray = freqArray.computeFrequencies(text,k)
		for i in range(4**k):
			if frequencyArray[i] >= t:
				clump[i] = 1
	for i in range(4**k):
		if clump[i] == 1:
			frequentPatterns.append(freqArray.NumberToPattern(i,k))
	return frequentPatterns

def betterClumpFinding(genome,k,t,L):
	frequentPatterns = []
	clump = [0] * (4**k)
	text = genome[0:L]
	frequencyArray = freqArray.computeFrequencies(text,k)
	for i in range(4**k):
		if frequencyArray[i] >= t :
			clump[i] = 1
	for i in range(1, len(genome) - L + 1):
		firstPattern = genome[i-1:i-1+k]
		index = freqArray.PatternToNumber(firstPattern)
		frequencyArray[index] = frequencyArray[index] - 1
		lastPattern = genome[i+L-k:i+L]
		index = freqArray.PatternToNumber(lastPattern)
		frequencyArray[index] = frequencyArray[index] + 1
		if frequencyArray[index] >= t:
			clump[index] = 1
	for i in range(4**k):
		if clump[i] == 1:
			frequentPatterns.append(freqArray.NumberToPattern(i,k))
	return frequentPatterns

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		genome = lines[0]
		nums = lines[1].split()
		k = int(nums[0])
		L = int(nums[1])
		t = int(nums[2])
	else:
		genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
		k = 5
		L = 50
		t = 4

	patterns = betterClumpFinding(genome,k,t,L)
	print ' '.join(patterns)