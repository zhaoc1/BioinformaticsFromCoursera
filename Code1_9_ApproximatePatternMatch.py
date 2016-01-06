"""
Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
     Input: Strings Pattern and Text along with an integer d.
     Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
"""
import sys,Code1_8_HammingDistance as hd

def approximate_pattern_match(pattern,text,d):
	idx = []
	k = len(pattern)
	for i in range(len(text)-k+1):
		if hd.hamming_distance(text[i:i+k],pattern) <= d:
			idx.append(i)
	return idx

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		pattern = lines[0]
		text = lines[1]
		d = int(lines[2])
	else:
		pattern = 'ATTCTGGA'
		text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
		d = 3
		
	idx = approximate_pattern_match(pattern,text,d)
	print ' '.join(map(str,idx))
