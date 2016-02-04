#Chunyu Zhao
# 20150721

import sys
def suffixArray(text):
	suffixes = []
	suffixarray = []
	for c in range(len(text)):
		suffixes.append(text[c:])
		suffixarray.append(c)
	suffixarray = [x for (y,x) in sorted(zip(suffixes,suffixarray))]
	suffixes.sort()
	return suffixarray,suffixes

if __name__ == '__main__':
	if len(sys.argv)==2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]
	else:
		text = "AACGATAGCGGTAGA$"
	suffixarray,suffixes = suffixArray(text)
	print ', '.join(map(str,suffixarray))