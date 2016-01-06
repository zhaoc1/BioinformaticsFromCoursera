"""
 CODE CHALLENGE: Solve the Frequent Words Problem.
     Input: A string Text and an integer k.
     Output: All most frequent k-mers in Text.
"""
#Chunyu Zhao 20150902

import sys,Code1_1_PatternCount as pc

def frequent_words(text,k):
	count = [0] * (len(text) - k + 1)
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		count[i] = pc.pattern_count(text,pattern)
	maxCount = max(count)
	freqPatterns = sorted(list(set([ text[i:i+k] for i,c in enumerate(count) if c == maxCount ])))
	return freqPatterns

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]
		k = int(lines[1])
	else:
		text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
		k = 4
		text = 'CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'
		k = 3

	freqPatterns = frequent_words(text,k)
	print ' '.join(freqPatterns)
