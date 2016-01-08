#Chunyu Zhao 20151108
import sys,math,Code4_8_NearestNeighbors as nn,Code4_7_SmallParsimonyUnrootedTree as spu,copy,Code4_6_SmallParsimony as sp
from collections import defaultdict

def nearest_neighbors_interchange(Tree,leaves):
	score = float("inf")
	newTree = copy.deepcopy(Tree)
	sp_ret, labels = spu.small_parsimony_unrooted(newTree,leaves)
	newScore = int(sp_ret[0])
	
	while newScore < score:
		score = newScore
		Tree = copy.deepcopy(newTree)

		'''find all the internal edge'''
		internalNodes = [node for node in Tree.keys() if len(Tree[node])==3]
		for istart in range(len(internalNodes)):
			for iend in range(istart+1,len(internalNodes)):
				a = internalNodes[istart]
				b = internalNodes[iend]
				if a in Tree[b] and b in Tree[a]:
					internalEdge = (a,b)
					Tree1,Tree2 = nn.nearest_neighbors(Tree,internalEdge)
					#for subtree one
					sp_ret,labels = spu.small_parsimony_unrooted(Tree1,leaves)
					neighborScore = int(sp_ret[0])
					if neighborScore<newScore:
						newScore = neighborScore
						newTree = copy.deepcopy(Tree1)
						newSpRet = sp_ret
						
					#for subtree second
					sp_ret,labels = spu.small_parsimony_unrooted(Tree2,leaves)
					neighborScore = int(sp_ret[0])
					if neighborScore<newScore:
						newScore = neighborScore
						newTree = copy.deepcopy(Tree2)
						newSpRet = sp_ret	
		print '\n'.join(newSpRet)
		print

if __name__ == "__main__":
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		n = int(lines[0])

		T = defaultdict(list)
		leaves = {}
		leaveNum = 0
		for i in range(1,len(lines)):
			nodei = lines[i].split('->')[0]
			nodej = lines[i].split('->')[1]
			if not nodei.isdigit():
				continue
			elif not nodej.isdigit():
				leaves[leaveNum] = nodej
				nodei = int(nodei)
				T[nodei].append(leaveNum)
				T[leaveNum].append(nodei)
				leaveNum += 1
			else:
				nodei = int(nodei)
				nodej = int(nodej)
				T[nodei].append(nodej)
		for node in T.keys():
			T[node] = sorted(T[node])
		nearest_neighbors_interchange(T,leaves)
