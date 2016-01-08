#Chunyu Zhao 20151126
import sys,math

class DepthFirstPaths():
	def __init__(self,tree):
		self.tree = tree
		self.edgeTo = dict((key,None) for key in self.tree.keys())
		self.marked = dict((key,False) for key in self.tree.keys())
		self.count = 0

	def dfs(self,v):
		self.count += 1
		self.marked[v] = True
		for w in self.tree[v]:
			if not self.marked[w]:
				self.edgeTo[w] = v
				self.dfs(w)

	def countLeaves(self,source):
		if len(self.tree[source]) == 0:
			return 1
		self.dfs(source)
		return (self.count+1)/2


def findClosestClusters(D):
	minValue = float('inf')
	for i in range(len(D)):
		for j in range(i+1,len(D)):
			if D[i][j] < minValue:
				minValue = D[i][j]
				closestClusters = (i,j)
	return closestClusters

def HierarchicalClustering(D):
	n = len(D)
	clusters = { node:[node] for node in range(n) }
	nodes = range(n)
	T = { node:[] for node in range(n) }
	
	while len(clusters) > 1:
		(ci,cj) = findClosestClusters(D)
		nodei = nodes[ci]
		nodej = nodes[cj]
		newCluster = clusters[nodei] + clusters[nodej]
		newCluster = [nc+1 for nc in newCluster]
		print ' '.join(map(str,newCluster))

		newNode = n
		n += 1

		newRow = []
		for m in range(len(D)):
			if m!= ci and m!=cj:
				cmi = D[m][ci]
				cmj = D[m][cj]
				leaveNumi = len(clusters[nodei])
				leaveNumj = len(clusters[nodej])
				newRow.append((cmi*leaveNumi+cmj*leaveNumj) / (leaveNumi+leaveNumj))
		newRow.append(0)

		Dnew = []
		for i in range(len(D)):
			if i!=ci and i!=cj:
				Dnew.append([D[i][j] for j in range(len(D[i])) if j != ci and j != cj])
		Dnew.append(newRow)
		for i in range(len(Dnew)-1):
			Dnew[i].append(Dnew[-1][i])
		D = Dnew

		T[newNode] = [nodes[ci], nodes[cj]]

		nodes.append(newNode)
		nodes = [nodes[i] for i in range(len(nodes)) if i !=ci and i != cj]
		clusters[newNode] = clusters[nodei] + clusters[nodej]
		clusters.pop(nodei)
		clusters.pop(nodej)
	
	root = clusters.keys()[0]
	T[root] = [clusters[root]]
	return T

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		n = int(lines[0])
		D = []
		nodes = range(n)
		for i in range(1,len(lines)):
			D.append(map(float,lines[i].strip().split(' ')))
	else:
		n = 7
		D = [[0.00, 0.74, 0.85, 0.54, 0.83, 0.92, 0.89],[0.74, 0.00, 1.59, 1.35, 1.20, 1.48, 1.55],\
		[0.85, 1.59, 0.00, 0.63, 1.13, 0.69, 0.73],[0.54, 1.35, 0.63, 0.00, 0.66, 0.43, 0.88],\
		[0.83, 1.20, 1.13, 0.66, 0.00, 0.72, 0.55],[0.92, 1.48, 0.69, 0.43, 0.72, 0.00, 0.80],\
		[0.89, 1.55, 0.73, 0.88, 0.55, 0.80, 0.00]]
	
	HierarchicalClustering(D)


if __name__ == '__main__':
	main()