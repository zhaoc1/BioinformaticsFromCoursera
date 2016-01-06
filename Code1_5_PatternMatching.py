"""
CODE CHALLENGE: Solve the Pattern Matching Problem.
     Input: Two strings, Pattern and Genome.
     Output: A collection of space-separated integers specifying all starting positions where Pattern appears
     as a substring of Genome.
"""
#Chunyu Zhao 20150904

import sys

def pattern_matching(pattern,genome):
	loc = []
	for i in range(len(genome) - len(pattern) + 1):
		if  pattern == genome[i:i+len(pattern)]:
			loc.append(i)
	return loc

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		pattern = lines[0]
		genome = lines[1]
	else:
		pattern = 'ATAT'
		genome = 'GATATATGCATATACTT'

	loc = pattern_matching(pattern,genome)
	print ' '.join(map(str,loc))
