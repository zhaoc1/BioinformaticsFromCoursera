__author__ = "Chunyu Zhao"
__date__ = "20160205"

import sys, BWT, BetterBWTMatching as BWTMatch,MultiplePatternMatching as mpm,partialSuffixArray

C = 5
K = 5

''' patterns are not always the same length'''

def hamming_distance(str1,str2):
	hd = 0
	minlen = min(len(str1),len(str2))
	maxlen = max(len(str1),len(str2))
	for i in range(minlen):
		if str1[i] != str2[i]:
			hd += 1
	hd += maxlen-minlen
	return hd

def multipleApproximatePatternMatching(text,patterns,d):
	lastC = BWT.BWT(text)
	firstOccur = BWTMatch.firstOccurrence(lastC)

	partialsuffixarray = partialSuffixArray.partialSuffixArray(text, K)
	checkpointarray = mpm.checkPointArray(lastC, C)
	suffixarray,suffixes = mpm.suffixArray(text)

	positions = []
	for pattern in patterns:
		'''seed preparation:divide pattern into d + 1 substring, with the length floor(n/(d+1))'''
		n = len(pattern)
		k = n / (d+1)
		#print "pattern",pattern,"n",n,"k",k,"d",d
		# for each pattern, if we hits same position in the text multiple times, we only keep one record.
		posstarts = []
		for i in range(d+1):
			if i == d:
				pat = pattern[i*k:]
			else:
				pat = pattern[i*k:(i+1)*k]
			'''seed detection: for each seed (pat), do exact pattern matching to find which seeds match Text exactly'''
			position = mpm.PatternMatching(suffixarray,firstOccur,lastC,checkpointarray,partialsuffixarray,pat)
			
			if position is not None:
				for pos in position:
					'''seed extension: extend seeds in both directions to verify whether Pattern occurs in Text with at most d mismatches.'''
					posstart = pos-k*i
					dist = hamming_distance(text[posstart:posstart+n],pattern)
					if dist is not None and dist <= d:
						posstarts.append(posstart)
		positions.extend(list(set(posstarts)))
	return positions

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]+"$"
		patterns = lines[1].split(' ')
		d = int(lines[2])
	else:
		text = "ACATGCTACTTT$"
		patterns = ["ATT","GCC","GCTA","TATT"]
		d = 1
	
	positions = multipleApproximatePatternMatching(text, patterns,d)
	print ' '.join(map(str,positions))
	