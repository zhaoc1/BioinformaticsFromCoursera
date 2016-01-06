"""
DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.
     Input: A collection of k-mers Patterns.
     Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
"""
#Chunyu Zhao 20150830

import sys

def build_deGruijnGraphFromKmers(kmers):
	kmers = sorted(kmers)
	''' we need to merge the prefix and suffix set in case there are single isolated edges! '''
	k_1mers = [k[:-1] for k in kmers] + [k[1:] for k in kmers]
	k_1mers = sorted(set(k_1mers))

	nodes = {}
	for i in range(len(k_1mers)):
		nodes[i] = k_1mers[i]
	invnodes = {v:k for k,v in nodes.items()}

	edges = {}
	for pat in kmers:
		prefixpat = pat[:-1]
		suffixpat = pat[1:]
		if invnodes[prefixpat] in edges:
			edges[invnodes[prefixpat]].append(invnodes[suffixpat])
		else:
			edges[invnodes[prefixpat]] = [invnodes[suffixpat]]

	temp = []
	for key, vals in edges.items():
		print nodes[key],'->',','.join([nodes[val] for val in vals])
		temp.append(nodes[key] +' -> '+','.join([nodes[val] for val in vals]))
	return temp

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		kmers = lines
	else:
		kmers = ['GAGG','CAGG','GGGG','GGGA','CAGG','AGGG','GGAG']

	temp = build_deGruijnGraphFromKmers(kmers)
