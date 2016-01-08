#Chunyu Zhao 20151111
import sys
from collections import defaultdict

massTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, \
			'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, \
			'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, \
			'V': 99, 'Y': 163,'X':4,'Z':5}

def ideal_spectrum(peptide):
	idealSpec = []
	for i in range(len(peptide)-1,-1,-1):
		idealSpec.append(get_mass(peptide[:i]))
		idealSpec.append(get_mass(peptide[i:]))
	return idealSpec

def get_mass(peptide):
	if len(peptide) == 0:
		return 0
	return sum([massTable[pep] for pep in peptide])

def spectrum_graph(Spectrum):
	Spectrum = sorted(Spectrum)
	specGraph = defaultdict(list)
	weighGraph = defaultdict(list)
	for i in range(len(Spectrum)):
		for j in range(i+1,len(Spectrum)):
			if Spectrum[j]-Spectrum[i] in massTable.values():
				aa = [ key for key,val in massTable.items() if val == Spectrum[j]-Spectrum[i]]
				specGraph[Spectrum[i]].append(Spectrum[j])
				weighGraph[Spectrum[i]].append(aa[0])
	specGraph[max(Spectrum)] = []
	weighGraph[max(Spectrum)] = []
	return specGraph,weighGraph

def decode_ideal_spec(spec):
	specGraph,weighGraph = spectrum_graph(spec)
	source = min(spec)
	sink = max(spec)
	edgeTo, marked,postorder = depthFirstPaths(specGraph,source)
	print specGraph
	print postorder[::-1]
	toposort = postorder[::-1]
	paths,peptides = pathTo(specGraph,weighGraph,source,sink,edgeTo)
	''' i dont know how to get all the paths....'''
	print paths
	peptide = []
	for i in range(len(paths)-1):
		peptide.append(weighGraph[paths[i]][specGraph[paths[i]].index(paths[i+1])])
	print ''.join(peptide)
		
	if sorted(ideal_spectrum(peptides)) == sorted(spec):
		print "true"
		return peptides

def depthFirstPaths(graph,s):
	nodes = graph.keys()
	edgeTo = dict((key,None) for key in graph.keys())
	marked = dict((key,False) for key in graph.keys())
	postorder = []
	edgeTo, marked,postorder = dfs(graph,s,edgeTo,marked,postorder)
	return edgeTo, marked,postorder

def dfs(graph,v,edgeTo,marked,postorder):
	marked[v] = True
	for w in graph[v]:
		if not marked[w]:
			edgeTo[w] = v
			edgeTo,marked,postorder = dfs(graph,w,edgeTo,marked,postorder)
	postorder.append(v)
	return edgeTo, marked,postorder

def pathTo(graph,weights,s,v,edgeTo):
	stack = []
	weightstack = []
	w = edgeTo[v]
	stack.append(v)
	weightstack.append(weights[w][graph[w].index(v)])
	while w != s:
		stack.append(w)
		v = w
		w = edgeTo[v]
		weightstack.append(weights[w][graph[w].index(v)])
	stack.append(s)
	return stack[::-1],''.join(weightstack[::-1])

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		Spectrum = map(int,lines[0].split(' '))
	else:
		Spectrum = [57,71,154,185,301,332,415,429,486]
	Spectrum = [0] + Spectrum
	print decode_ideal_spec(Spectrum)