#Chunyu Zhao 20150909

import sys,Code1_8_HammingDistance as hd

def immediateNeighbor(pattern):
	neighbor = [pattern]
	for i in range(len(pattern)):
		symbol = pattern[i]
		for x in ['A','C','G','T']:
			if x != symbol:
				neighbor.append(pattern[:i]+x+pattern[i+1:])
	return neighbor

def neighbors(pattern,d):
	if d == 0:
		return pattern
	if len(pattern) == 1:
		return ['A','C','G','T']

	neighborhood = []
	suffixNeighbors = neighbors(pattern[1:],d)
	for text in suffixNeighbors:
		if hd.hamming_distance(pattern[1:],text) < d:
			for x in ['A','C','G','T']:
				neighborhood.append(x+text)
		else:
			neighborhood.append(pattern[:1]+text)
	neighborhood = list(set(neighborhood))
	return neighborhood

def approximatePatternCount(text,pattern,d):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if hd.hamming_distance(text[i:i+len(pattern)],pattern) <= d:
			count += 1
	return count

def frequentWordsWithMismatches(text,k,d):
	frequentPatterns = []
	close = [0] * (4**k)
	frequencyArray = [0] * (4**k)
	for i in range(len(text)-k+1):
		neighborhood = neighbors(text[i:i+k],d)
		for pattern in neighborhood:
			index = PatternToNumber(pattern)
			close[index] = 1
	'''only consider k-mers that are close to a k-mer in text'''
	for i in range(4**k):
		if close[i] == 1:
			pattern = NumberToPattern(i,k)
			frequencyArray[i] = approximatePatternCount(text,pattern,d)
	
	maxCount = max(frequencyArray)
	for i in range(4**k):
		if frequencyArray[i] == maxCount:
			pattern = NumberToPattern(i,k)
			frequentPatterns.append(pattern)
	return list(set(frequentPatterns))

def frequentWordsWithMismatchesBySorting(text,k,d):
	neighborhoods = []
	for i in range(len(text)-k+1):
		reverseString = reverse_complement(text[i:i+k])
		neighborhoods = neighborhoods + neighbors(text[i:i+k],d) + neighbors(reverseString,d)
	
	count = [0] * len(neighborhoods)
	index = [0] * len(neighborhoods)
	for i in range(len(neighborhoods)):
		pattern = neighborhoods[i]
		index[i] = PatternToNumber(pattern)
		count[i] = 1

	sortedIndex = sorted(index)
	for i in range(len(neighborhoods)-1):
		if sortedIndex[i] == sortedIndex[i+1]:
			count[i+1] = count[i] + 1
	maxCount = max(count)
	frequentPatterns = [NumberToPattern(sortedIndex[i],k) for i,c in enumerate(count) if c == maxCount]
	return frequentPatterns

def SymbolToNumber(symbol):
	mapping = {'A':0,'C':1,'G':2,'T':3}
	return mapping[symbol]

def NumberToSymbol(number):
	mapping = {'A':0,'C':1,'G':2,'T':3}
	invmapping = {val:key for key, val in mapping.items()}
	return invmapping[number]

def PatternToNumber(pattern):
	''' beautiful recursion '''
	if len(pattern) == 0 :
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def NumberToPattern(index,k):
	if k == 1:
		return NumberToSymbol(index)
	prefixIndex = index / 4
	r = index % 4
	symbol = NumberToSymbol(r)
	prefixPattern = NumberToPattern(prefixIndex, k-1)
	return prefixPattern + symbol

def reverse_complement(dna):
	dnadict = {'A':'T','C':'G','G':'C','T':'A'}
	reverseDna = [ dnadict[c] for c in dna ]
	return ''.join(reverseDna[::-1])

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]
		k = int(lines[1].split(' ')[0])
		d = int(lines[1].split(' ')[1])
	else:
		text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
		k = 4
		d = 1

	print "Frequent Words with Mismatches Problem:"
	freqpattern = frequentWordsWithMismatches(text,k,d)
	print ' '.join(freqpattern)

	print "Frequent Words with Mismatches and Reverse Complements Problem:"
	freqpattern = frequentWordsWithMismatchesBySorting(text,k,d)
	print ' '.join(freqpattern)
