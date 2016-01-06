"""
CODE CHALLENGE: Implement PatternCount:
     Input: Strings Text and Pattern.
     Output: Count(Text, Pattern).
"""
#Chunyu Zhao 20150902

import sys

def pattern_count(text,pattern):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if text[i:i+len(pattern)] == pattern:
			count +=1
	return count

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]
		pattern = lines[1]
	else:
		text = 'GCGCG'
		pattern = 'GCG'
		text = 'CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC'
		pattern = 'CGCG'
	
	count = pattern_count(text,pattern)
	print count
