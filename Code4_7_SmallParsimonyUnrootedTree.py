#Chunyu Zhao 20151107
import sys, Code4_6_SmallParsimony as sp,math,copy
from collections import defaultdict

def small_parsimony_unrooted(Tree,leaves):
	T = copy.deepcopy(Tree)
	nodes = T.keys()
	root = len(nodes)
	'''take the last node as default the maximal node num, add root to it'''
	nodei = len(nodes)-1
	nodej = max(T[len(nodes)-1])

	T[nodei].remove(nodej)
	T[nodej].remove(nodei)
	T[root].append(nodei)
	T[root].append(nodej)
	T[nodei].append(root)
	T[nodej].append(root)
	
	cols = zip(*leaves.values())
	ret = []
	scores = 0
	n = len(leaves)
	for i in range(len(leaves[0])):
		Character = dict(zip(range(n),cols[i]))
		score,col = sp.small_parsimony(T,Character)
		ret.append(col.values())
		scores += score
	
	finalCharacter = dict(zip(T.keys(),zip(*ret)))
	result = printTree(T,finalCharacter,scores)
	return result,finalCharacter

def printTree(T,Character,scores):
	print_ret = []
	finalCharacter = {}
	source = max(T.keys())
	distTo,edgeTo = sp.bfs(T,source)
	nodes = sorted(T.keys(),reverse=True)

	nodei = T[source][0]
	nodej = T[source][1]
	str0 = ''.join(Character[source])
	str1 = ''.join(Character[nodei])
	str2 = ''.join(Character[nodej])

	scores -= sp.hamming_distance(str0,str1)
	scores -= sp.hamming_distance(str0,str2)
	scores += sp.hamming_distance(str1,str2)

	print_ret.append(str(scores))

	for node in nodes:
		if node == source:
			continue
		finalCharacter[node] = ''.join(Character[node])
		path = sp.pathTo(node,distTo,edgeTo)
		parent = path[1]
		if parent == source:
			continue
		str1 = ''.join(Character[node])
		str2 = ''.join(Character[parent])
		print_ret.append(str1+'->'+str2+':'+str(sp.hamming_distance(str1,str2)))
		print_ret.append(str2+'->'+str1+':'+str(sp.hamming_distance(str1,str2)))
	nodei = T[source][0]
	nodej = T[source][1]
	str0 = ''.join(Character[source])
	str1 = ''.join(Character[nodei])
	str2 = ''.join(Character[nodej])
	print_ret.append(str1+'->'+str2+':'+str(sp.hamming_distance(str1,str2)))
	print_ret.append(str2+'->'+str1+':'+str(sp.hamming_distance(str1,str2)))
	return print_ret

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
		for i in range(2,2*n+1,2):
			node = int(lines[i].split('->')[0])
			string = lines[i].split('->')[1]
			leaves[i/2-1] = string
			T[node].append(i/2-1)
			T[i/2-1] = []
		for j in range(2*n+2,len(lines),2):
			T[int(lines[j].split('->')[0])].append(int(lines[j].split('->')[1]))
		small_parsimony_unrooted(T,leaves)