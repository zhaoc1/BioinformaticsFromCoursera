#Chunyu Zhao 20150914

import sys

def hamming_distance(str1,str2):
	hd = 0
	if len(str1) != len(str2):
		print "the two strings different length ERROR"
		return None
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			hd += 1
	return hd

def medianString(dna,k):
	distance = float('inf')
	for i in range(4**k):
		pattern = NumberToPattern(i,k)
		if distance > distanceBetweenPatternAndStrings(pattern,dna):
			distance = distanceBetweenPatternAndStrings(pattern,dna)
			median = pattern
	return median

def distanceBetweenPatternAndString(pattern,text):
	distance = float('inf')
	for i in range(len(text)-len(pattern)+1):
		hd = hamming_distance(pattern,text[i:i+len(pattern)])
		if hd < distance:
			distance = hd
			motif = text[i:i+len(pattern)]
	return distance

def distanceBetweenPatternAndStrings(pattern,strings):
	k = len(pattern)
	distance = 0
	for i in range(len(strings)):
		distance += distanceBetweenPatternAndString(pattern,strings[i])
	return distance

def SymbolToNumber(symbol):
	mapping = {'A':0,'C':1,'G':2,'T':3}
	return mapping[symbol]

def NumberToSymbol(number):
	mapping = {'A':0,'C':1,'G':2,'T':3}
	invmapping = {val:key for key, val in mapping.items()}
	return invmapping[number]

def PatternToNumber(pattern):
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

if __name__ == '__main__':
	if len(sys.argv)==2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		#pattern = lines[0]
		#strings = lines[1].split(' ')
		k = int(lines[0])
		dna = lines[1:]
	else:
		#pattern = 'AAA'
		#strings = ['TTACCTTAAC','GATATCTGTC','ACGGCGTTCG','CCCTAAAGAG','CGTCAGAGGT']
		k = 3
		dna = ['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTTCGGGACAG']
		
	#distanceBetweenPatternAndStrings(pattern,strings)
	medianstring = medianString(dna,k)
	print medianstring