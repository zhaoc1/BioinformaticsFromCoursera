#Chunyu Zhao 20151025
from collections import defaultdict
import sys

def update_graph(graph):
	nodes = graph.keys()
	for node in graph.keys():
		links = graph[node]
		for link in links:
			if link[0] not in nodes:
				nodes.append(link[0])
	''' make graph complete with only in-going nodes'''
	for node in nodes:
		if node not in graph.keys():
			graph[node] = []
	return graph,nodes

def acyclicLP(graph,s,v):
	global postorder,marked,nodes,distTo,edgeTo
	graph,nodes = update_graph(graph)
	edgeTo = {node:None for node in nodes}
	distTo = {node:float("-inf") for node in nodes}
	distTo[s] = 0
	depthFirstOrder(graph)
	topo_order = postorder[::-1]
	for node in topo_order:
		for edge in graph[node]:
			relax(node,edge[0],edge[1])
	pathsTOv = pathTo(graph,s,v)
	return distTo[v],pathsTOv

def relax(start,end,weight):
	global distTo,edgeTo
	if distTo[end] < distTo[start] + weight:
		distTo[end] = distTo[start] + weight
		edgeTo[end] = start

def depthFirstOrder(graph):
	global postorder, marked, nodes
	''' set up variables '''
	postorder = []#queue FIFO
	marked = {node:False for node in nodes}
	for v in graph.keys():
		if not marked[v]:
			dfs(G,v)

def dfs(graph,v):
	global postorder, marked
	marked[v] = True
	for nodew in graph[v]:
		w = nodew[0]
		if not marked[w]:
			dfs(graph,w)
	postorder.append(v)

def pathTo(graph,s,v):
	global edgeTo
	stack = []
	w = edgeTo[v]
	stack.append(v)
	while w != s:
		stack.append(w)
		v = w
		w = edgeTo[v]
	stack.append(s)
	return stack[::-1]

if __name__ == '__main__':
	if len(sys.argv)==2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		s = int(lines[0])
		v = int(lines[1])
		G = defaultdict(list)
		for line in lines[2:]:
			nodei = int(line.split("->")[0])
			nodej = int(line.split("->")[1].split(':')[0])
			w = int(line.split("->")[1].split(':')[1])
			G[nodei].append((nodej,w))
	else:
		s = 0
		v = 4
		G = {0:[(1,7),(2,4)],2:[(3,2)],1:[(4,1)],3:[(4,3)]}

	longest, path = acyclicLP(G,s,v)
	print '->'.join(map(str,path))
