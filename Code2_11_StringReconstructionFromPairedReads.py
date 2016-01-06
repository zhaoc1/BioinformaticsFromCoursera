"""
CODE CHALLENGE: Solve the String Reconstruction from Read-Pairs Problem.
     Input: Integers k and d followed by a collection of paired k-mers PairedReads.
     Output: A string Text with (k, d)-mer composition equal to PairedReads.
"""
#Chunyu Zhao 20150910
import sys, Code2_10_StringSpelledByGappedGenomePath as gappedString, Code2_7_EulerianPath as eupath

def build_deGruijnGraphFromPairedKmers(pairedKmers):
	# remove the white space in the end of some lines
	pairedKmers = [pk.strip() for pk in pairedKmers]
	# first need to sork the pairedKmers
	kmers = [pk.replace('|','') for pk in pairedKmers]
	sortedIndex = sorted(range(len(kmers)), key=lambda k: kmers[k])
	# extract the prefix and suffix of both the first and second part of the kmers separated by '|'
	sortedKmers = [pairedKmers[i] for i in sortedIndex]

	k_1mers = []
	for kmer in sortedKmers:
		kmer = kmer.split('|')
		k_1mers.append(kmer[0][:-1]+'|'+kmer[1][:-1])
		k_1mers.append(kmer[0][1:]+'|'+kmer[1][1:])

	k_1mers = sorted(set(k_1mers))

	nodes = {}
	for i in range(len(k_1mers)):
		nodes[i] = k_1mers[i]
	invnodes = {v:k for k,v in nodes.items()}

	edges = {}
	for pat in pairedKmers:
		pat = pat.split('|')
		node1 = pat[0][:-1]+'|'+pat[1][:-1]
		node2 = pat[0][1:]+'|'+pat[1][1:]
		if invnodes[node1] in edges:
			edges[invnodes[node1]].append(invnodes[node2])
		else:
			edges[invnodes[node1]] = [invnodes[node2]]

	adjlist = {}
	temp = []
	for key, vals in edges.items():
		adjlist[key] = vals
	return adjlist,nodes

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		k = int(lines[0].split()[0])
		d = int(lines[0].split()[1])
		pairedKmers = lines[1:]
		
	adjlist,nodes = build_deGruijnGraphFromPairedKmers(pairedKmers)
	print "number of nodes:",len(nodes)
	numedge = 0
	for v in adjlist.keys():
		numedge += len(adjlist[v])
	print "number of outgoing edges:",numedge

	path = eupath.eulerian_path(adjlist)
	patterns = [nodes[p] for p in path]
	string = gappedString.stringSpelledByGappedPatterns(patterns,k,d)
	print string
