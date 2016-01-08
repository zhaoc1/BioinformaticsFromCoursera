#Chunyu Zhao 20151029
from __future__ import division
import sys
from collections import defaultdict

''' as an UPGMA tree, the degree of internal nodes must be three SOGA'''
'''20151030: it took me a while to realize that it is the number of leaves in a cluster, not the number of nodes'''
def dfs(tree,v,edgeTo,marked,count):
	count += 1
	marked[v] = True
	for w in tree[v]:
		if not marked[w]:
			edgeTo[w] = v
			edgeTo,marked,count = dfs(tree,w,edgeTo,marked,count)
	return edgeTo, marked,count

def count(tree,s):
	if len(tree[s]) == 0:
		return 1
	'''edgeTo and marked all save the index of nodes'''
	edgeTo = dict((key,None) for key in tree.keys())
	marked = dict((key,False) for key in tree.keys())
	count = 0
	edgeTo, marked,count = dfs(tree,s,edgeTo,marked,count)
	return (count+1)/2#THE NUMBER OF LEAVES:) n + n - 1 = count

def upgma1(D,nodes):
	#create the tree first
	T = {}
	age = {}
	for node in nodes:
		T[node] = []
		age[node] = 0

	nodeNum = len(D)
	while len(nodes)>1:
		cv,ci,cj = findMin(D) #ci, cj are the index of D
		newnode = nodeNum
		nodeNum += 1

		newRow = []
		for m in range(len(D)):
			if m!=ci and m!=cj:
				cmi = D[m][ci]
				cmj = D[m][cj]
				numi = count(T,nodes[ci])
				numj = count(T,nodes[cj])
				newRow.append((cmi*numi+cmj*numj) / (numi+numj))
		newRow.append(0)

		T[nodes[ci]].append(newnode)
		T[nodes[cj]].append(newnode)
		T[newnode] = [nodes[ci], nodes[cj]]
		age[newnode] = cv/2.0
		
		Dnew = []
		for i in range(len(D)):
			if i != ci and i != cj:
				Dnew.append([D[i][j] for j in range(len(D[i])) if j != ci and j != cj])
		nodes = [nodes[i] for i in range(len(nodes)) if i !=ci and i != cj]		
		nodes.append(newnode)
		Dnew.append(newRow)
		for i in range(len(Dnew)-1):
			Dnew[i].append(Dnew[-1][i])
		D = Dnew

	for v in T.keys():
		T[v] = [ (w,abs(age[v]-age[w])) for w in T[v] ] 
	return T

def findMin(D):
	'''return the row and column index of the min value, not necessarily the node number'''
	n = len(D)
	imin = None
	jmin = None
	vmin = float("inf")
	for i in range(n):
		rowmin = min([x for x in D[i] if x>0])
		if rowmin < vmin:
			imin = i
			jmin = D[i].index(rowmin)
			vmin = rowmin
	return (vmin,imin,jmin)

def printTree(T):
	for v in T.keys():
		for (w,edge) in T[v]:
			print str(v)+"->"+str(w)+":"+"%.3f"%(edge)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		n = int(lines[0])
		D = []
		nodes = range(n)
		for i in range(1,len(lines)):
			D.append(map(int,lines[i].strip().split(' ')))
	else:
		n = 4
		D =[[0,20,17,11],[20,0,20,13],[17,20,0,10],[11,13,10,0]]
		nodes = range(n)

	tree = upgma1(D,nodes)
	printTree(tree)