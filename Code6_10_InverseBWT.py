# 20160722
#! /usr/bin/env python
__author__      = "Chunyu Zhao"
import sys, numpy

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

def iBWT(last):
	first,countFirst,last,countLast = firstFromLast(last)

	string = ['$']
	nextrow = [r for r,c in enumerate(last) if c == "$"]
	nextrow = nextrow[0]
	string.append(first[nextrow])

	while len(string)<len(last):
		nextrow = [r for r,c in enumerate(last) if c == first[nextrow] and countLast[r] == countFirst[nextrow]]
		nextrow = nextrow[0]
		string.append(first[nextrow])
	string = string[1:]+string[:1]
	return "".join(string)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		lastColumn = lines[0]
	else:
		lastColumn = "TTCCTAACG$A"
	ibwt = iBWT(lastColumn)
	print ibwt
		