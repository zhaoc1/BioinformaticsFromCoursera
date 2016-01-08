#Chunyu Zhao 20151021

import sys
from collections import defaultdict

#to simplify the question, we assume all the leaves index come before the ancestors
# easy to fix, nodes.index(leavei)

def distancesBeteweenLeaves(tree):
	leaves = [ node for node in tree.keys() if len(tree[node]) == 1]
	nodes = tree.keys()
	dist_matrix = [[0]*len(leaves) for _ in range(len(leaves))]
	for i in range(len(leaves)):
		for j in range(i,len(leaves)):
			edgeTo, marked = depthFirstPaths(tree,leaves[i])
			
			if leaves[j] != leaves[i]:
				#print "leave[i]",leaves[i],"leave[j]",leaves[j]
				pathij,dij = pathTo(tree,weights,leaves[j],leaves[i],edgeTo)
				dist_matrix[leaves[i]][leaves[j]] = dij
				dist_matrix[leaves[j]][leaves[i]] = dij
	return dist_matrix

def depthFirstPaths(tree,s):
	nodes = tree.keys()
	edgeTo = [None] * len(nodes)
	marked = [False] * len(nodes)
	edgeTo, marked = dfs(tree,s,edgeTo,marked)
	return edgeTo, marked

def dfs(tree,v,edgeTo,marked):
	marked[v] = True
	for w in tree[v]:
		if not marked[w]:
			edgeTo[w] = v
			edgeTo,marked = dfs(tree,w,edgeTo,marked)
	return edgeTo, marked

def pathTo(tree,weights,v,s,edgeTo):
	stack = []
	dij = 0
	w = edgeTo[v]
	stack.append(v)
	while w != s:
		stack.append(w)
		dij += weights[w][tree[w].index(v)]
		v = w
		w = edgeTo[v]
	stack.append(s)
	dij += weights[s][tree[s].index(v)]
	return stack[::-1],dij

if __name__ == '__main__':
	if len(sys.argv)==2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		n = int(lines[0])#
		tree = {}
		weights = {}
		for line in lines[1:]:
			nodei = int(line.split("->")[0])
			nodej = int(line.split("->")[1].split(':')[0])
			w = int(line.split("->")[1].split(':')[1])
			if nodei in tree:
				tree[nodei].append(nodej)
				weights[nodei].append(w)
			else:
				tree[nodei] = [nodej]
				weights[nodei] = [w]

	distMat = distancesBeteweenLeaves(tree)
	print '\n'.join([ ' '.join(map(str,dist)) for dist in distMat ])
