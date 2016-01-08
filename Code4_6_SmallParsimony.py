#Chunyu Zhao 20151107
import sys,math
from collections import defaultdict

def hamming_distance(str1,str2):
	hd = 0
	if len(str1) != len(str2):
		return None
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			hd += 1
	return hd

def small_parsimony(T,Character):
	alphabet = 'ACGT'
	Tag = {}
	s = {}

	source = max(T.keys())
	distTo,edgeTo = bfs(T,source)

	for v in T.keys():
		if len(T[v]) == 1:
 			Tag[v] = 1
			s[v] = [float('inf')] * 4
			s[v][alphabet.index(Character[v])] = 0
		else:
			Tag[v] = 0

	while len([tag for tag in Tag.values() if tag == 0 ]) > 0 :
		nodes = sorted(distTo,key=distTo.get,reverse=True)
		'''start to find ripe internal nodes:'''
		tag0node = [node for node in nodes if Tag[node]==0]
		if len(tag0node) == 1:
			v = tag0node[0]
		else:
			vs = []
			for node in tag0node:
				child_ripe = [ child for child in T[node] if Tag[child] == 1]
				if len(child_ripe) == len(T[node])-1:
					vs.append(node)
			v = vs[0]	
		Tag[v] = 1
		s[v] = [None]*4
		for k in alphabet:
			children = [child for child in T[v] if distTo[child] > distTo[v]]
			#print "children",children,"T[v]",T[v],[distTo[child] for child in T[v]]
			daughter = children[0]
			son = children[1]

			if s[daughter][alphabet.index(k)] == min(s[daughter]):
				delta_ik = 0
			else:
				delta_ik = 1
			if s[son][alphabet.index(k)] == min(s[son]):
				delta_jk = 0
			else:
				delta_jk = 1
			s[v][alphabet.index(k)] = min(s[daughter]) + min(s[son]) + delta_jk + delta_ik
	
	parsimonyScore = min(s[v])
	Character[source] = alphabet[s[source].index(min(s[source]))]
	''' sort the nodes based on the distTo value!!! '''
	distTo,edgeTo = bfs(T,source)
	nodes = sorted(distTo,key=distTo.get)
	for node in nodes:
		if node not in Character.keys():
			path = pathTo(node,distTo,edgeTo)
			parent = path[1]
			if s[node][alphabet.index(Character[parent])] == min(s[node]):
				Character[node] = Character[parent]
			else:
				Character[node] = alphabet[s[node].index(min(s[node]))]
	return parsimonyScore,Character

def bfs(G,s):
	queue = []
	distTo = dict(zip(G.keys(),[None] * len(G.keys())))
	marked = dict(zip(G.keys(),[None] * len(G.keys())))
	edgeTo = dict(zip(G.keys(),[None]*len(G.keys())))
	
	distTo[s] = 0
	queue.append(s)
	marked[s] = True
	
	while len(queue) != 0:
		v = queue.pop()
		for w in G[v]:
			if marked[w] is None:
				edgeTo[w] = v
				distTo[w] = distTo[v] + 1
				marked[w] = True
				queue.append(w)
	return distTo,edgeTo

def pathTo(v,distTo,edgeTo):
	stack = []
	x = v
	while distTo[x]!=0:
		stack.append(x)
		x = edgeTo[x]
	stack.append(x)
	return stack

def printTree(T,Character):
	source = max(T.keys())
	distTo,edgeTo = bfs(T,source)
	nodes = sorted(T.keys(),reverse=True)
	for node in nodes:
		if node == source:
			continue
		path = pathTo(node,distTo,edgeTo)
		parent = path[1]
		str1 = ''.join(Character[node])
		str2 = ''.join(Character[parent])
		print str1+'->'+str2+':'+str(hamming_distance(str1,str2))
		print str2+'->'+str1+':'+str(hamming_distance(str1,str2))


if __name__ == "__main__":
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		n = int(lines[0])
		h = math.log(n,2)
		totalNodes = int(2**(h+1) - 1)
		T = defaultdict(list)
		leaves = {}
		for i in range(1,n+1):
			node = int(lines[i].split('->')[0])
			string = lines[i].split('->')[1]
			leaves[i-1] = string
			T[node].append(i-1)
			T[i-1] = []
		for i in range(n+1,len(lines)):
			T[int(lines[i].split('->')[0])].append(int(lines[i].split('->')[1]))
	else:
		n = 4
		h = math.log(n,2)
		totalNodes = int(2**(h+1) - 1)
		leaves = {0:'CAAATCCC',1:'ATTGCGAC',2:'CTGCGCTG',3:'ATGGACGA'}
		T = {0:[],1:[],2:[],3:[],4:[0,1],5:[2,3],6:[4,5]}
		
		
	cols = zip(*leaves.values())
	ret = []
	scores = 0
	for i in range(len(leaves[0])):
		Character = dict(zip(range(n),cols[i]))
		score,col = small_parsimony(T,Character)
		ret.append(col.values())
		scores += score
	print scores
	finalCharacter = dict(zip(T.keys(),zip(*ret)))
	printTree(T,finalCharacter)
