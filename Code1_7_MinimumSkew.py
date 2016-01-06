"""
 Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.
     Input: A DNA string Genome.
     Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
"""
import sys

def get_skew(genome):
	skew = [0] * (len(genome)+1)
	for i in range(len(genome)):
		if genome[i] == 'G':
			skew[i+1] = skew[i] + 1;
		elif genome[i] == 'C':
			skew[i+1] = skew[i] - 1;
		else:
			skew[i+1] = skew[i]
	return skew

def min_skew(skew):
	minval = min(skew)
	minidx = [i for i,v in enumerate(skew) if v == minval]
	return minidx

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		genome = lines[0]
	else:
		genome = 'CATTCCAGTACTTCATGATGGCGTGAAGA'

	skew = get_skew(genome)
	org = min_skew(skew)
	print ' '.join(map(str,org))