__author__ = "Chunyu Zhao"
#20150723
import sys, numpy

def lastToFirst(last):
	ret = []
	first,countFirst,last,countLast = firstFromLast(last)
	for pos in range(len(last)):
		i = [r for r,c in enumerate(first) if c == last[pos] and countLast[pos] == countFirst[r]]
		i = i[0]
		ret.append(i)
	return ret

def BWMatching(lastColumn,pattern):
	LastToFirst = lastToFirst(lastColumn)
	rowFirst = range(0,len(lastColumn))
	top = min(rowFirst)
	bottom = max(rowFirst)
	while top <= bottom:
		if len(pattern) > 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]
			rowLast = [r for r in rowFirst if lastColumn[r] == symbol]
			if len(rowLast) > 0:
				rowFirst = [LastToFirst[r] for r in rowLast]
				top = min(rowFirst)
				bottom = max(rowFirst)
			else:
				return 0
		else:
			return bottom - top + 1

def firstFromLast(last):
	first = sorted(last)
	countFirst = []
	mapping = {}
	for c in first:
		mapping[c] = mapping.get(c,0) + 1
		countFirst.append(mapping[c])
	
	countLast = []
	mapping = {}
	for c in last:
		mapping[c] = mapping.get(c,0) + 1
		countLast.append(mapping[c])
	return first,countFirst,last,countLast


if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		lastColumn = lines[0]
		pattern = lines[1].split(" ")
	else:
		lastColumn = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC"
		pattern = ["CCT","CAC","GAG","CAG","ATC"]
		
	ret = []
	for pat in pattern:
		ret.append(BWMatching(lastColumn,pat))
	print ' '.join(map(str,ret))

