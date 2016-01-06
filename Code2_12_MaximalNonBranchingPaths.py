"""
Contig Generation Problem: Generate the contigs from a collection of reads (with imperfect coverage).
     Input: A collection of k-mers Patterns. 
     Output: All contigs in DeBruijn(Patterns).
"""
#Chunyu Zhao 20150907

import sys

"""
MaximalNonBranchingPaths(Graph)
        Paths <- empty list
        for each node v in Graph
            if v is not a 1-in-1-out node
                if out(v) > 0
                    for each outgoing edge (v, w) from v
                        NonBranchingPath <- the path consisting of the single edge (v, w)
                        while w is a 1-in-1-out node
                            extend NonBranchingPath by the outgoing edge (w, u) from w 
                            w <- u
                        add NonBranchingPath to the set Paths
        for each isolated cycle Cycle in Graph
            add Cycle to Paths
        return Paths
"""
def prepareGraph(adjlist):
	nodes = [node for edges in adjlist.values() for node in edges] + adjlist.keys()
	nodes = sorted(set(nodes))

	indegree = dict(zip(nodes,[0]*len(nodes)))
	outdegree = dict(zip(nodes,[0]*len(nodes)))
	for v in adjlist:
		outdegree[v] = len(adjlist[v])
		for w in adjlist[v]:
			indegree[w] += 1

	newadjlist = {}
	for v in nodes:
		if v in adjlist.keys():
			newadjlist[v] = adjlist[v]
		else:
			newadjlist[v] = []
	return nodes, indegree, outdegree,newadjlist

def maximalNonBranchingPaths(adjlist):
	paths = []
	nodes, indegree, outdegree,newadjlist = prepareGraph(adjlist)
	for v in nodes:
		if indegree[v]!= 1 or outdegree[v]!=1:
			if outdegree[v] > 0:
				for w in adjlist[v]: #v->w
					nonbranchingpath = [v,w]
					while indegree[w] == 1 and outdegree[w] == 1:
						u = adjlist[w][0]
						nonbranchingpath.append(u)
						w = u
					paths.append(nonbranchingpath)
	return paths

'''still didn't really understand the recursion...'''
def directedCycle(adjlist):
	nodes,indegree,outdegree,adjlist = prepareGraph(adjlist)
	marked = dict(zip(nodes,[None]*len(nodes)))
	onStack = dict(zip(nodes,[None]*len(nodes)))
	edgeTo = dict(zip(nodes,[None]*len(nodes)))
	cycles = []
	for node in adjlist.keys():
		if not marked[node]:
			dfs(adjlist,node,marked,onStack,edgeTo,cycles)
	return cycles

def dfs(graph,vertex,marked,onStack,edgeTo,cycles):
    onStack[vertex] = True
    marked[vertex] = True
    cycle = []
    for neighbour in graph[vertex]:
        if len(cycle)>0:
        	return cycles
        elif not marked[neighbour]:
            edgeTo[neighbour] = vertex
            dfs(graph,neighbour,marked,onStack,edgeTo,cycles)
        elif onStack[neighbour]:
        	x = vertex
        	while x != neighbour:
        		cycle.append(x)
        		x = edgeTo[x]
        	cycle.append(neighbour)
        	cycle.append(vertex)
        	cycle = cycle[::-1]
        	cycles.append(cycle)
    onStack[vertex] = False

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		adjlist = {}
		for line in lines:
			line = line.split(' -> ')
			edges = map(int,line[1].split(','))
			adjlist[int(line[0])] = edges
	else:
		adjlist = {1:[2],2:[3],3:[4,5],6:[7],7:[6]}

	maxpath = maximalNonBranchingPaths(adjlist)
	for path in maxpath:
		print ' -> '.join(map(str,path))
	