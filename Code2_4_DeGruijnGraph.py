"""
CODE CHALLENGE: Solve the De Bruijn Graph from a String Problem.
     Input: An integer k and a string Text.
     Output: DeBruijnk(Text), in the form of an adjacency list.
"""
#Chunyu Zhao 20150830

import sys

def build_deGruijnGraph(text,k):
	''' first get the unique k-1 mers, which are in fact the nodes of the De Gruijn Graph '''
	k_1mers = []
	for i in range(len(text)-k+2):
		k_1mers.append(text[i:i+k-1])

	k_1mers = sorted(list(set(k_1mers)))
	''' generate nodes'''
	nodes = {}
	for i,v in enumerate(k_1mers):
		nodes[i] = v
	invnodes = {v:i for i,v in nodes.items()}
	''' adding edges based on the overlapping graph of k-1 mers '''
	edges = {}
	for i in range(len(text)-k+1):
		if invnodes[text[i:i+k-1]] in edges:
			edges[invnodes[text[i:i+k-1]]].append(invnodes[text[i+1:i+k]])
		else:
			edges[invnodes[text[i:i+k-1]]] = [invnodes[text[i+1:i+k]]]
	''' print out the result '''
	temp = []
	for key,vals in edges.items():
		print nodes[key],'->',','.join(sorted([nodes[val] for val in vals]))
		temp.append( nodes[key]+' -> '+','.join(sorted([nodes[val] for val in vals])) )
	return temp

if len(sys.argv) == 2:
	filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	k = int(lines[0])
	text = lines[1]
else:
	text = 'AAGATTCTCTAAGA'
	k = 4
	
temp = build_deGruijnGraph(text,k)
