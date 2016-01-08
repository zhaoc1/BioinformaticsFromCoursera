#Chunyu Zhao 20151108
import sys,copy,smallParsimony as sp
from collections import defaultdict

def nearest_neighbors(T,internalEdge):
	a = internalEdge[0]
	b = internalEdge[1]
	startChild = [t for t in T[a] if t != b]
	endChild = [t for t in T[b] if t != a and t not in startChild]
	w = startChild[0]
	x = startChild[1]
	y = endChild[0]
	z = endChild[1]
	#nearest tree one
	T1 = copy.deepcopy(T)
	T1[a].remove(x)
	T1[x].remove(a)
	T1[b].remove(y)
	T1[y].remove(b)

	T1[a].append(y)
	T1[y].append(a)
	T1[b].append(x)
	T1[x].append(b)
	#nearest tree second
	
	T2 = copy.deepcopy(T)
	T2[a].remove(x)
	T2[x].remove(a)
	T2[a].append(z)
	T2[z].append(a)

	T2[b].remove(z)
	T2[z].remove(b)
	T2[b].append(x)
	T2[x].append(b)
	return T1,T2

def print_tree(T):
	for nodei in T.keys():
		for nodej in T[nodei]:
			print str(nodei)+'->'+str(nodej)

	
if __name__ == "__main__":
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		a = int(lines[0].split(' ')[0])
		b = int(lines[0].split(' ')[1])
		
		T = defaultdict(list)
		for i in range(1,len(lines)):
			nodei = int(lines[i].split('->')[0])
			nodej = int(lines[i].split('->')[1])
			T[nodei].append(nodej)
		
		T1,T2 = nearest_neighbors(T,(a,b))
		print_tree(T1)
		print 
		print_tree(T2)