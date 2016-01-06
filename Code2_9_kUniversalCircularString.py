"""
CODE CHALLENGE: Solve the k-Universal Circular String Problem.
     Input: An integer k.
     Output: A k-universal circular string.
"""
#Chunyu Zhao 20150902

import sys, Code2_5_DeGruijnGraphFromkmers2 as degraph, Code2_6_EulerianCycle as eucycle
from itertools import product

if len(sys.argv) == 2:
	filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	k = int(lines[0])
else:
	k = 4

if __name__ == '__main__':
	kmers = [ ''.join(x) for x in product('01', repeat=k) ]
	adjlist,nodes = degraph.build_deGruijnGraphFromKmers(kmers)
	cycle = eucycle.eulerian_cycle(adjlist)

	length = 2**k
	epath = [nodes[p] for p in cycle]
	string = [epath[0]]
	for pa in epath[1:]:
		string.append(pa[-1])
	uni_string  = ''.join(string)
	uni_string = uni_string[:length]
	print uni_string
