"""
EULERIANCYCLE(Graph)
        form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
        while there are unexplored edges in Graph
            select a node newStart in Cycle with still unexplored edges
            form Cycle' by traversing Cycle (starting at newStart) and then randomly walking 
            Cycle <- Cycle'
        return Cycle
"""
# Chunyu Zhao 20150831
# Runs in O(E+V) time

import sys,random

"""
1. Choose any vertex v and push it onto a stack. Initially all EDGEs are unmarked.
2. While the stack is nonempty, look at the top vertex, u, on the stack. If u has an
unmarked incident edge, say, to a vertex w, then push w onto the stack and mark the
edge uw. On the other hand, if u has no unmarked incident edge, then pop u off the
stack and print it.
"""

def eulerian_cycle(adjlist):
	nodes = adjlist.keys()
	eulerianCycle = []

	marked = {} # we need to mark the EDGE
	edges = 0
	for key,val in adjlist.items():
		marked[key] = [False] * len(val)
		edges += len(val)
	# choose any vertex v and push it onto stack
	v = random.choice(nodes)
	# greedily add to cycle, depth-first search style
	stack = []
	stack.append(v)
	# while the stack is not empty
	while len(stack):
		u = stack[-1]
		unmarkedEdges = [i for i,mark in enumerate(marked[u]) if mark == False]
		if len(unmarkedEdges):
			w = adjlist[u][unmarkedEdges[0]]
			marked[u][unmarkedEdges[0]] = True
			stack.append(w)
		else:
			del stack[-1]
			eulerianCycle.append(u)
	return eulerianCycle[::-1]

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
		adjlist = {0:[3],1:[0],2:[1,6],3:[2],4:[2],5:[4],6:[5,8],7:[9],8:[7],9:[6]}

	cycle = eulerian_cycle(adjlist)
	printcycle = ''.join([str(c) + '->' for c in cycle])
	print printcycle[:-2]