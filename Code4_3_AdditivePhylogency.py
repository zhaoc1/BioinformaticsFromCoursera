__author__ = 'Chunyu'

import os
from limb import limbLength
from itertools import permutations
from collections import defaultdict
'''refer to the additive_phylogency's idea about add branch and I need to master this concept.'''

def additive_phylogence(D,n):
	global Tree
	global nodesnum
	if n == 2:
		Tree = defaultdict(list)
		Tree[0].append((1,D[0][1]))
		Tree[1].append((0,D[0][1]))
		return
	limblen = limbLength(D,n-1)
	'''calculate D_bald to find out (i,L,k)'''
	for j in range(n-1):
		D[j][n-1] = D[j][n-1]-limblen
		D[n-1][j] = D[j][n-1]
	ik = [l for l in range(len(D[n-1][:-1])) if D[n-1][l]!=0]
	for i,k in permutations(ik,2):
		if i < k and D[i][n-1] + D[k][n-1] == D[i][k]:
			x = D[i][n-1]
			ret = ((i,x),(n-1,limblen),(k,D[i][k]-x))
			break
	'''calculate D_trimmed'''
	D = D[0:n-1][0:n-1]
	'''recursively'''
	additive_phylogence(D,n-1)
	'''FORMAT: ret = ((i,x),(l,limblen),(k,D[i][k]-x))'''
	pathiTok = pathBetweenLeaves(Tree,ret[0][0],ret[2][0])
	x = ret[0][1]
	l = ret[1][0]
	limblen = ret[1][1]
	start_node = ret[0][0]
	for node, dist in pathiTok:
		if dist ==0:
			continue
		if x > dist:
			x -= dist
			start_node = node
		elif x == dist:
			Tree[node].append((l,limblen))
			Tree[l].append((node,limblen))
			break
		elif x < dist:
			'''this part is reallly good'''
			new_node = nodesnum
			nodesnum += 1
			Tree[new_node].append((l,limblen))
			Tree[l].append((new_node,limblen))
			Tree[start_node].remove((node,dist))
			Tree[node].remove((start_node,dist))
			Tree[start_node].append((new_node,x))
			Tree[new_node].append((start_node,x))
			Tree[node].append((new_node,dist-x))
			Tree[new_node].append((node,dist-x))
			break

def pathBetweenLeaves(graph,i,k):
	tree = defaultdict(list)
	weights = defaultdict(list)
	for nodei,childList in graph.items():
		for j in range(len(childList)):
			tree[nodei].append(childList[j][0])
			weights[nodei].append(childList[j][1])
	edgeTo, marked = depthFirstPaths(tree,i)
	path = pathTo(tree,weights,k,i,edgeTo)
	return path

def depthFirstPaths(tree,s):
	'''edgeTo and marked all save the idnex of nodes'''
	edgeTo = dict((key,None) for key in tree.keys())
	marked = dict((key,False) for key in tree.keys())
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
	w = edgeTo[v]
	stack.append((v,weights[w][tree[w].index(v)]))
	while w != s:
		v = w
		w = edgeTo[v]
		stack.append((v,weights[w][tree[w].index(v)]))
	stack.append((s,0))
	return stack[::-1]

def limbLength(mat,j):
	n = len(mat)
	leaves = range(n)
	leavesLeft = [l for l in leaves if l != j]
	minlen = float("inf")
	for i,k in permutations(leavesLeft,2):
		if i < k:
			lenik = (mat[j][i]+mat[j][k]-mat[i][k]) / 2
			if lenik < minlen:
				minlen = lenik
	return minlen

if __name__ == '__main__':
    os.chdir('/Users/April/Documents/BioinformaticsAlgorithm/4.DecipheringMolecularEvolution')
    with open('dataset_10330_6.txt', 'r') as f:
        lines = f.read().splitlines()
    n = int(lines[0])####
    D = []
    for l in lines[1:]:
    	D.append(map(int,l.split()))
    #D = [[0,13,21,22],[13,0,12,13],[21,12,0,13],[22,13,13,0]]
    #n = 4
    global Tree
    global nodesnum
    nodesnum = n
    additive_phylogence(D,n)
    for key,vals in Tree.items():
    	for val in vals:
        	print str(key)+'->'+str(val[0])+':'+str(val[1])
