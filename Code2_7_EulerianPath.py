"""
CODE CHALLENGE: Solve the Eulerian Path Problem.
     Input: The adjacency list of a directed graph that has an Eulerian path.
     Output: An Eulerian path in this graph.
"""
import sys, eulerianCycle

def eulerian_path(adjlist):
	# for those nodes with only ingoing edges and no outgoing edges need EXTRA attention!
	nodes = adjlist.keys()
	morenodes = []
	for u in adjlist.values():
		morenodes = morenodes + u
	nodes = list(set(nodes + morenodes))

	indegree = dict( zip(nodes,[0] * len(nodes) ))
	outdegree = dict( zip(nodes,[0] * len(nodes) ))
	for key,vals in adjlist.items():
		outdegree[key] += len(vals)
		for val in vals:
			indegree[val] += 1

	for node in nodes:
		if indegree[node] > outdegree[node]:
			end = node
		elif indegree[node] < outdegree[node]:
			start = node

	if end in adjlist:
		adjlist[end].append(start)
	else:
		adjlist[end] = [start]

	euleriancycle = eulerianCycle.eulerian_cycle(adjlist)
	# we need to locate the added EDGE, not only the startpos
	startpos = [i for i,v in enumerate(euleriancycle) if v == start]
	endpos = [i for i,v in enumerate(euleriancycle) if v == end]
	for pos1 in startpos:
		for pos2 in endpos:
			if pos1-pos2 == 1:
				startpos = pos1
	eulerianpath =  euleriancycle[startpos:] + euleriancycle[1:startpos]
	
	return eulerianpath

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		adjlist = {}
		for line in lines:
			node = int(line.split(' -> ')[0])
			edge = map(int,line.split(' -> ')[1].split(','))
			adjlist[node] = edge
	else:
		adjlist = {0:[2],1:[3],2:[1],3:[0,4],6:[3,7],7:[8],8:[9],9:[6]}

	path = eulerian_path(adjlist)
	printpath = ''.join([str(c) + '->' for c in path])
	print printpath[:-2]