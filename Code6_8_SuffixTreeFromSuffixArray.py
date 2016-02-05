#Chunyu Zhao 20150721
"""
We need to where the path representing the (i+1)th suffix (SuffixArray[i+1]) "splits" from the already 
constructed partial suffix tree SuffixTree_i(Text).
"""

"""
Constructing Suffix Tree from Suffix Array Problem: Construct a suffix tree from the suffix array and LCP array of a string. 
Input: A string Text, SuffixArray(Text), and LCP(Text).
Output: SuffixTree(Text).
STOP and THINK: how in linear time?
"""

import sys
def constructSuffixTreeFromSuffixArray(text,suffixarray,lcp):
	nodecount = 0 #root
	s = nodecount
	suffixtree = {s:[]}
	edge = {s:[]}
	parenttree = {s:None}
	descent = {s:0}
	x = 0 # for the SuffixTree_1: i = 0, SuffixTree_2: i = 1
	"""
	we will walk up the rightmost path
	:= the last added path in the partial suffix tree
	:= previously added LEAF, labeled SuffixArray(i)
	"""
	for i in range(len(text)):
		v = x # ALSO: [node for node, edgelabel in edge.iteritems() if edgelabel[0] == suffixarray[i-1]]
		while descent[v] > lcp[i]:
			v = parenttree[v]

		if descent[v] == lcp[i]:
			# add a new leaf x: (v, x)
			nodecount += 1
			x = nodecount
			xStart = suffixarray[i]+lcp[i]
			suffixtree[v].append(x)
			edge[v].append(text[xStart:])
			parenttree[x] = v
			descent[x] = descent[v] + len(text[xStart:])
			suffixtree[x] = [None]
			edge[x] = [suffixarray[i]]
		elif descent[v] < lcp[i]:
			w = suffixtree[v][-1]
			# 1. delete edge (v,w) from the suffixtree(text)
			del suffixtree[v][-1]
			del edge[v][-1]
			# 2. add a new internal node y: (v, y)
			nodecount += 1
			y = nodecount
			suffixtree[v].append(y)
			parenttree[y] = v
			suffixtree[y] = []
			edge[y] = []
			yStart = suffixarray[i] + descent[v]
			yEnd = suffixarray[i] + lcp[i]
			edge[v].append(text[yStart:yEnd])
			# 3. update descent(y)
			descent[y] = lcp[i]
			# 4. connect w to y: (y, w)
			suffixtree[y].append(w)
			parenttree[w] = y
			wStart = suffixarray[i-1] + lcp[i]
			wEnd = suffixarray[i-1] + descent[w]
			edge[y].append(text[wStart:wEnd])		
			# 5. add a new leaf x: (y, x)
			nodecount += 1
			x = nodecount
			suffixtree[y].append(x)
			parenttree[x] = y
			suffixtree[x] = [None]
			edge[x] = [suffixarray[i]]
			xStart = suffixarray[i] + lcp[i]
			edge[y].append(text[xStart:])
			descent[x] = descent[y] + len(text[xStart:])
	#print "suffixtree",suffixtree,"\n"
	#print "edge",edge,"\n"
	#print "descent",descent,"\n"
	return suffixtree, edge

def printSuffixTree(suffixtree,edge):
	for node in suffixtree.keys():
		if suffixtree[node][0] is not None:
			for child in range(len(suffixtree[node])):
				print edge[node][child]


def suffixArray(text):
	suffixes = []
	suffixarray = []
	for c in range(len(text)):
		suffixes.append(text[c:])
		suffixarray.append(c)
	suffixarray = [x for (y,x) in sorted(zip(suffixes,suffixarray))]
	suffixes.sort()
	return suffixarray,suffixes

"""
Depth-first orders: Depth-first search search visits each vertex exactly once. 
Three vertex orderings are of interest in typical applications:
Preorder: Put the vertex on a queue before the recursive calls.
"""
def preorder(G, s=0):
	marked = [None] * len(G)
	preorder = []
	for v in G.keys():
		if marked[v] is None:
			dfs(G,v,preorder)
	return preorder
			
def dfs(G, v,preorder):
	marked[v] = True
	preorder.append(v)
	for w in G[v]:
		if marked[w] is None:
			queue.append(v)
			dfs(G,w)
	postorder.append(v)


"""
Longest common prefix (LCP) array of Text, LCP(Text), which stores the length of the longest common prefix 
shared by consecutive lexicographically ordered suffixes of Text. 
For example, LCP("panamabananas$") is (0, 0, 1, 1, 3, 3, 1, 0, 0, 0, 2, 2, 0, 0), as shown below.
"""
def LCP(suffix):
	print "inside"
	lcparray = [0] * (len(suffix))
	for c in range(1,len(suffix)):
		lcparray[c] = lcp(suffix[c-1],suffix[c])
	#print "lcparray",lcparray,"\n"
	return lcparray

def lcp(str1, str2):
	"""least commone prefix, REFER to String.java"""
	N = min(len(str1),len(str2))
	for c in range(N):
		if str1[c] != str2[c]:
			return c
	return N

def leastRepeatedString(suffix):
	lrs = []
	for c in range(len(suffix)-1):
		length = lcp(suffix[c],suffix[c+1])
		if length > len(lrs):
			lrs = suffix[c][:length]
	return lrs

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]
		line1 = lines[1].split(",")
		suffixarray = [int(l) for l in line1]
		line2 = lines[2].split(",")
		lcp = [int(l) for l in line2]
	else:
		text = "GTAGT$"
		suffixarray = [5,2,3,0,4,1]
		lcp = [0,0,0,2,0,1]

		text = "panamabananas$"
		suffixarray,suffixes = suffixArray(text)
		print "suffixarray",suffixarray,"\n"
		print "suffixes",suffixes,"\n"
		lcp = LCP(suffixes)

	suffixtree, edge = constructSuffixTreeFromSuffixArray(text,suffixarray,lcp)
	printSuffixTree(suffixtree,edge)

if __name__ == '__main__':
	main()
