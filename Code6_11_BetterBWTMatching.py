__author__   = "Chunyu Zhao"
# 20150722
import sys, numpy

def countMatrix(last):
	mapping = sorted(set(last))
	symbolDict = {k:v for v, k in enumerate(mapping)}
	count = numpy.zeros(((len(last)+1), len(mapping)), dtype=numpy.int)
	for i in range(len(last)):
		count[i+1] = count[i]
		count[i+1][symbolDict[last[i]]] = count[i][symbolDict[last[i]]] + 1
	count = count.tolist()
	return count

def firstOccurrence(last):
	unilast = sorted(set(last))
	first = sorted(last)
	vec = [0] * len(unilast)
	for i,c in enumerate(unilast):
		vec[i] = [j for j,s in enumerate(first) if s == c][0]
	return vec

def BetterBWMatching(lastColumn,pattern):
	countMat = countMatrix(lastColumn)
	firstOccur = firstOccurrence(lastColumn)

	top = 0
	bottom = len(lastColumn) - 1
	while top <= bottom:
		if len(pattern) > 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]
			if lastColumn[top:bottom].count(symbol) > 0:
				top = firstOccur['$ACGT'.index(symbol)] + countMat[top]['$ACGT'.index(symbol)]
				bottom = firstOccur['$ACGT'.index(symbol)] + countMat[bottom+1]['$ACGT'.index(symbol)] - 1
			else:
				return 0
		else:
			return bottom - top + 1


if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		lastColumn = lines[0]
		pattern = lines[1].split(" ")
	else:
		lastColumn = "GGCGCCGC$TAGTCACACACGCCGTA"
		pattern = ["ACC","CCG","CAG"]

	ret = []
	for pat in pattern:
		ret.append(BetterBWMatching(lastColumn,pat))
	print " ".join(map(str,ret))

