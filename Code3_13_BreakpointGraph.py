#Chunyu Zhao 20151118

import sys

def two_break_on_genome_path(graph,i1,i2,j1,j2):
	graph[i1].remove(i2)
	graph[j1].remove(j2)
	graph[i2].append(j1)
	graph[i1].append(j2)
	return graph

def chromosome_cycle(chromosome):
	nodes = [0] * len(chromosome)*2
	for j in range(1,len(chromosome)+1):
		i = chromosome[j-1]
		if i>0:
			nodes[2*j-1-1] = 2*i-1
			nodes[2*j-1] = 2*i
		else:
			nodes[2*j-1-1] = -2 * i
			nodes[2*j-1] = -2 * i -1
	return nodes

def cycle_chromosome(nodes):
	chromosome = [0] * (len(nodes)/2)
	for j in range(1,len(nodes)/2+1):
		if nodes[2*j-1-1] < nodes[2*j-1]:
			chromosome[j-1] = nodes[2*j-1]/2
		else:
			chromosome[j-1] = -nodes[2*j-1-1]/2
	return chromosome

def colored_edges(P):
	edges = []
	for chromosome in P:
		chromosome = map(int,chromosome.split(' '))
		nodes = chromosome_cycle(chromosome)
		for j in range(len(chromosome)):
			if (nodes[2*j-1],nodes[2*j]) not in edges:
				edges.append((nodes[2*j-1],nodes[2*j]))
	return edges

def read_graph(edges):
	n = len(edges)*2
	graph = {node:[] for node in range(1,n+1)}
	for edge in edges:
		edge = edge.split(', ')
		nodei = int(edge[0])
		nodej = int(edge[1])
		graph[nodei].append(nodej)
	'''undirected black edge'''
	for j in range(1,len(edges)+1):
		graph[2*j-1].append(2*j)
		graph[2*j].append(2*j-1)
	return graph

def edge_graph(edges):
	n = max(map(max,edges))
	graph = {node:[] for node in range(1,n+1)}
	for edge in edges:
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])
	for j in range(1,n/2+1):
		graph[2*j-1].append(2*j)
		graph[2*j].append(2*j-1)
	return graph

def find_cycle(graph):
	nodes = graph.keys()
	edgeTo = dict((key,None) for key in nodes)
	marked = dict((key,False) for key in nodes)
	onStack = dict((key,False) for key in nodes)

	cycles = []
	for node in nodes:
		if not marked[node]:
			cycles = dfs(graph,node,edgeTo,marked,onStack,cycles)
	return cycles

def dfs(graph,v,edgeTo,marked,onStack,cycles):
	marked[v] = True
	onStack[v] = True
	for w in graph[v]:
		cycle = []
		if not marked[w]:
			edgeTo[w] = v
			dfs(graph,w,edgeTo,marked,onStack,cycles)
		elif onStack[w]: #aha: cycle
			x = v
			while x != w:
				cycle.append(x)
				x = edgeTo[x]
			cycle.append(w)
			cycle.append(v)
			cycle = cycle[::-1]
			if len(cycle)>3:
				cycles.append(cycle)
	onStack[v] = False
	return cycles

def graph_genome(graph):
	cycles = find_cycle(graph)
	P = []
	for cycle in cycles:
		if abs(cycle[0]-cycle[1]) == 1:
			cycle = cycle[:-1]
		else:
			cycle = cycle[1:]
		chromosome = cycle_chromosome(cycle)
		P.append(chromosome)
	return P

def print_graph(P):
	printP = []
	for p in P:
		printP.append("(%s)" % ' '.join("%+d" % e for e in p) )
	return printP

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		E = lines[0]
	else:
		#P = '(+1 -2 -3 +4)'
		#P = '(1 2 4 3 6 5 7 8)'
		#P = '(+1 -2 -3)(+4 +5 -6)'
		E = '(2, 4), (3, 8), (7, 5), (6, 1), (10, 12), (11, 8)'
		P = '(+1 -2)(-3 +4)'
		P = '(+1 -2 -3 +4)'
	
	E = E.strip().lstrip('(').rstrip(')').split('), (')
	G = read_graph(E)
	print "G",G
	P = graph_genome(G)
	print P
	print ''.join(print_graph(P))
	
	'''
	nodes = chromosome_cycle(P)
	print "(%s)" % ' '.join("%d" % e for e in nodes)
	chromosome = cycle_chromosome(P)
	print "(%s)" % ' '.join("%+d" % e for e in chromosome)
	
	P = P.strip().lstrip('(').rstrip(')').split(')(')
	print P
	edges = colored_edges(P)
	print "%s" % ', '.join("("+str(e[0])+", "+str(e[1])+")" for e in edges)
	'''

	'''
	edges =  colored_edges(P)
	graph = edges_graph(edges)
	graph2 = copy.deepcopy(graph)
	graph2 = two_break_on_genome_path(graph2,i1,i2,j1,j2)
	P = graph_genome(graph2)
	printP = []
	for p in P:
		printP.append("(%s)" % ' '.join("%+d" % e for e in p) )
	print ''.join(printP)
	
	E = E.strip().lstrip('(').rstrip(')').split('), (')
	G = read_graph(E)
	newG = two_break_on_genome_path(G,i1,i2,j1,j2)
	print_graph(newG)
	'''
