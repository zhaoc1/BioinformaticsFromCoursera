"""
CODE CHALLENGE: Solve the Overlap Graph Problem (restated below).
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.
"""
#Chunyu Zhao 20150829

import sys

def form_graph(patterns):
	nodes = {}
	edges = {}
	for i in range(len(patterns)):
		nodes[i] = patterns[i]
		edges[i] = []
	return nodes,edges

def add_edge(patterns):
	temp = []
	nodes,edges = form_graph(patterns)
	k = len(patterns[0])
	for i in range(len(patterns)):
		# check for in-going edges, aka prefix
		prefix = patterns[i][:k-1]
		ingoingNodes = [pat.find(prefix,1) for pat in patterns]
		ingoingNodes = [loc for loc,inode in enumerate(ingoingNodes) if inode >0]
		if len(ingoingNodes):
			for ingoingNode in ingoingNodes:
				edges[ingoingNode].append(i)
		# check for out-going edges, aka suffix
		# pattern[1:]
		# pattern.find(pat,start = 1)
	for key, vals in edges.items():
		if len(vals):
			for val in vals:
				print nodes[key], '->', nodes[val]
				temp.append(nodes[key] + ' -> ' + nodes[val])
	return temp

if len(sys.argv) == 2:
	filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	patterns = lines
else:
	patterns = ['ATGCG','GCATG','CATGC','AGGCA','GGCAT']

patterns = sorted(patterns)
temp = add_edge(patterns)