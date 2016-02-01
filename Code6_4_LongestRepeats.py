#Chunyu Zhao 20151129
import sys
from SuffixTreeConstruction import SuffixTree

class BreadthFirstPaths(object):
	def __init__(self,tree,text):
		self.tree = tree
		self.text = text
		self.edgeTo = dict((key,None) for key in self.tree.nodes.keys())
		self.marked = dict((key,False) for key in self.tree.nodes.keys())
		self.distTo = dict((key,float('inf')) for key in self.tree.nodes.keys())
		self.pathTo = dict((key,None) for key in self.tree.nodes.keys())
		self.count = 0

	def bfs(self,s):
		queue = []
		self.distTo[s] = 0
		self.marked[s] = True
		self.pathTo[s]= ''
		queue.append(s)

		while len(queue) != 0:
			v = queue.pop(0)
			for w in self.tree.nodes[v].child:
				if self.marked[w] is False:
					queue.append(w)
					self.marked[w] = True
					self.edgeTo[w] = v
					self.distTo[w] = self.distTo[v] + 1

					idx = self.tree.nodes[v].child.index(w)
					position = self.tree.nodes[v].edge[idx][0]
					length = self.tree.nodes[v].edge[idx][1]
					edgeString = self.text[position:position+length]
					self.pathTo[w] = self.pathTo[v] + edgeString

def longestRepeats(text):
	suffixTree = SuffixTree(text)
	suffixTree.modifiedSuffixTreeConstruction()
	bfpath = BreadthFirstPaths(suffixTree,text)
	bfpath.bfs(0)
	longestPath = ''
	for i in suffixTree.nodes.keys():
		node = suffixTree.nodes[i]
		if len(node.child) > 0:
			currentPath =  bfpath.pathTo[i]
			if len(currentPath) > len(longestPath):
				longestPath = currentPath
	print longestPath
	
if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		test1 = lines[0]+'#'
		test2 = lines[1]+'$'
	else:
		text = 'ATATCGTTTTATCGTT$'
	longestRepeats(text)