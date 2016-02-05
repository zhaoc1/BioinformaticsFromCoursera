__author__ = "Chunyu Zhao"
__date__ = "20150723"

import sys

def suffixArray(text):
	suffixes = []
	suffixarray = []
	for c in range(len(text)):
		suffixes.append(text[c:])
		suffixarray.append(c)
	suffixarray = [x for (y,x) in sorted(zip(suffixes,suffixarray))]
	return suffixarray

def partialSuffixArray(text,K):
	suffixarray = suffixArray(text)
	partialsuffixarray = {}
	for i, s in enumerate(suffixarray):
		if s % K ==0:
			partialsuffix = i
			partialsuffixarray[i] = s
	return partialsuffixarray

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]
		K = int(lines[1])
	else:
		text = "PANAMABANANAS$"
		K= 5 
		suffixArray(text)

	ret = partialSuffixArray(text, K)
	for key in ret:
		print str(key)+','+str(ret[key])
