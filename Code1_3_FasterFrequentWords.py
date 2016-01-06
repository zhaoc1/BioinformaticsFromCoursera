
#Chunyu Zhao 20150902

import sys

"""RECURSION: PatToNum(Pattern) = 4 * PatToNum(Prefix(Pattern)) + SymbolToNumber(LastSymbol(Pattern))"""
def PatternToNumber(pattern):
	if len(pattern) == 0 :
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def SymbolToNumber(symbol):
	mapping = {'A':0,'C':1,'G':2,'T':3}
	return mapping[symbol]

def NumberToSymbol(number):
	mapping = {'A':0,'C':1,'G':2,'T':3}
	invmapping = {val:key for key, val in mapping.items()}
	return invmapping[number]

def NumberToPattern(index,k):
	if k == 1:
		return NumberToSymbol(index)
	prefixIndex = index / 4
	r = index % 4
	symbol = NumberToSymbol(r)
	prefixPattern = NumberToPattern(prefixIndex, k-1)
	return prefixPattern + symbol
	
def computeFrequencies(text,k):
	frequencyArray = [0] * (4**k)
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		j = PatternToNumber(pattern)
		frequencyArray[j] += 1
	return frequencyArray

def fasterFrequentWords(text,k):
	frequencyArray = computeFrequencies(text,k)
	maxCount = max(frequencyArray)
	frequentPatterns = [NumberToPattern(i,k) for i, c in enumerate(frequencyArray) if c == maxCount]
	return frequentPatterns

def findingFrequentWordsBySorting(text,k):
	index = [0] * (len(text)-k+1)
	count = [0] * (len(text)-k+1)
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		index[i] = PatternToNumber(pattern)
		count[i] = 1
	sortedIndex = sorted(index)
	''' very nice '''
	for i in range(1,len(text)-k+1):
		if sortedIndex[i] == sortedIndex[i-1]:
			count[i] = count[i-1] + 1
	
	maxCount = max(count)
	frequentPatterns = [NumberToPattern(sortedIndex[i],k) for i,c in enumerate(count) if c == maxCount]
	return frequentPatterns

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]
		k = int(lines[1])
	else:
		text = 'ACGCGGCTCTGAAA'
		k = 2

	frequencyArray = computeFrequencies(text,k)
	print ' '.join(map(str,frequencyArray))
	
	print ' '.join(fasterFrequentWords(text,k))
	print ' '.join(findingFrequentWordsBySorting(text,k))

