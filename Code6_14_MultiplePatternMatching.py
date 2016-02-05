__author__ = 'Chunyu Zhao'
#20150723,20160204

import sys, BWT, BetterBWTMatching as BWTMatch, partialSuffixArray

C = 5
K = 5
def multiplePatternMatching(text, patterns):
	"""Input that I can use: LastColumn, FirstOccurrence, CheckPointArray, PartialSuffixArray"""
	lastC = BWT.BWT(text)
	firstOccur = BWTMatch.firstOccurrence(lastC)

	partialsuffixarray = partialSuffixArray.partialSuffixArray(text, K)
	checkpointarray = checkPointArray(lastC, C)
	suffixarray,suffixes = suffixArray(text)

	positions = []
	for pattern in patterns:
		position = PatternMatching(suffixarray,firstOccur,lastC,checkpointarray,partialsuffixarray,pattern)
		if position is not None:
			for pos in position:
				positions.append(pos)
	return positions

def suffixArray(text):
	suffixes = []
	suffixarray = []
	for c in range(len(text)):
		suffixes.append(text[c:])
		suffixarray.append(c)
	suffixarray = [x for (y,x) in sorted(zip(suffixes,suffixarray))]
	suffixes.sort()
	return suffixarray,suffixes

def PatternMatching(suffixarray,firstOccur,lastC,checkpointarray,partialsuffixarray,pattern):
	top,bottom = BetterBWMatching(firstOccur,lastC,checkpointarray,partialsuffixarray,pattern)
	if top is None:
		return None
	position = suffixarray[top:bottom+1]
	return position
	
def BetterBWMatching(firstOccur,lastC,checkpointarray,partialsuffixarray,pattern):
	top = 0
	bottom = len(lastC)-1

	while top<=bottom:
		if len(pattern) > 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]
			if lastC[top:bottom+1].count(symbol) > 0:	
				top = firstOccur['$ACGT'.index(symbol)] + countMatrix(lastC,checkpointarray,top,symbol)
				bottom = firstOccur['$ACGT'.index(symbol)] + countMatrix(lastC,checkpointarray,bottom+1,symbol) - 1
			else:
				return None,None
		else:
			return top,bottom

def countMatrix(lastC,checkpointarray,idx,symbol):
	'''implement countMat[index]['ACGT'.index(symbol)] based on checkpointarray'''
	idxStart = (idx/C)*C
	rank = checkpointarray[idxStart]['$ACGT'.index(symbol)]
	if lastC[idxStart:idx].count(symbol)>0:
		count = lastC[idxStart:idx].count(symbol)
		rank = rank + count
	return rank

def checkPointArray(last, C):
	countmatrix = BWTMatch.countMatrix(last)
	checkpointarray = {}
	for i, c in enumerate(countmatrix):
		if i % C == 0 :
			checkpointarray[i] = c
	return checkpointarray

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]+"$"
		patterns = lines[1:]
	else:
		text = "AATCGGGTTCAATCGGGGT$"
		patterns = ["ATCG", "GGGT"]
	
	positions = multiplePatternMatching(text, patterns)
	print ' '.join(map(str,positions))