from __future__ import division
import sys
from collections import defaultdict
#Chunyu Zhao 20151031

def neighbor_joining(D,nodes):
	global nodeNum
	n = len(D)
	if n == 2:
		T = defaultdict(list)
		T[nodes[0]].append((nodes[1],D[0][1]))
		T[nodes[1]].append((nodes[0],D[1][0]))
		return T
	Dstar = getDstar(D)
	ci,cj = findMin(Dstar)

	newnode = nodeNum
	nodeNum += 1
	totalDist = [ sum(row) for row in D ]
	delta = (totalDist[ci] - totalDist[cj])/ (n-2)
	limbi = (D[ci][cj] + delta) / 2.0
	limbj = (D[ci][cj] - delta) / 2.0
	nodei = nodes[ci]
	nodej = nodes[cj]

	newRow = [(D[k][ci]+D[k][cj]-D[ci][cj])/2.0 for k in range(n) if k!=ci and k!=cj]
	newRow.append(0)
	Dnew = []
	for i in range(n):
		if i != ci and i != cj:
			Dnew.append([D[i][j] for j in range(len(D[i])) if j != ci and j != cj])
	nodes = [nodes[i] for i in range(len(nodes)) if i !=ci and i != cj]		
	nodes.append(newnode)
	Dnew.append(newRow)
	for i in range(n-2):
		Dnew[i].append(Dnew[-1][i])
	D = Dnew

	''' recursively '''
	T = neighbor_joining(D,nodes)

	T[nodei].append((newnode,limbi))
	T[nodej].append((newnode,limbj))
	T[newnode].append((nodei,limbi))
	T[newnode].append((nodej,limbj))

	return T

def getDstar(D):
	n = len(D)
	totalDist = [ sum(row) for row in D ]
	Dstar = []
	for i in range(n):
		Dstar.append([(n-2)*D[i][j]-totalDist[i]-totalDist[j] for j in range(n)])
	for i in range(n):
		for j in range(n):
			if i==j:
				Dstar[i][j] = 0
	return Dstar

def findMin(D):
	'''return the row and column index of the min value, not necessarily the node number'''
	n = len(D)
	imin = None
	jmin = None
	vmin = float("inf")
	for i in range(n):
		rowmin = min([x for x in D[i] if x != 0])
		if rowmin < vmin:
			imin = i
			jmin = D[i].index(rowmin)
			vmin = rowmin
	return (imin,jmin)

def printTree(T):
	for v in T.keys():
		for (w,edge) in T[v]:
			print str(v)+"->"+str(w)+":"+"%.2f"%(edge)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		n = int(lines[0])
		D = []
		nodes = range(n)
		for i in range(1,n+1):
			D.append(map(int,lines[i].strip().split(' ')))
	else:
		n = 4
		D =[[0,23,27,20],[23,0,30,28],[27,30,0,30],[20,28,30,0]]
		nodes = range(n)

	global nodeNum 
	nodeNum = n
	T = neighbor_joining(D,nodes)
	printTree(T)