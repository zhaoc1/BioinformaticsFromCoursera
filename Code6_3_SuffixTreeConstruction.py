#Chunyu Zhao 20151128
import sys
from collections import defaultdict

class SuffixTrie(object):
	radix = 5
	class Node(object):
		def __init__(self,number):
			self.number = number
			self.child = [None]*SuffixTrie.radix
			self.position = [None]*SuffixTrie.radix

	def __init__(self,text):
		self.nodes = [self.Node(0)]
		self.N = 1 #number of nodes in Trie
		self.text = text

	def constructSuffixTrie(self):
		for i in xrange(len(self.text)):
			currentNode = self.nodes[0] #root
			for j in xrange(i,len(self.text)):
				currentSymbol = self.text[j]
				currentSymbolIndex = 'ACGT$'.index(currentSymbol)
				if currentNode.child[currentSymbolIndex] is None:
					newNode = self.Node(self.N)
					self.nodes.append(newNode)
					currentNode.child[currentSymbolIndex] = newNode.number
					currentNode.position[currentSymbolIndex] = j
					self.nodes[currentNode.number] = currentNode
					self.N += 1
					currentNode = newNode
				else:
					currentNode = self.nodes[currentNode.child[currentSymbolIndex]]
			if len( [child for child in currentNode.child if child is not None] ) < 1:
				currentNode.position = i
				self.nodes[currentNode.number] = currentNode


	def put(self,pattern):
		currentNode = self.nodes[0] #root
		for ci in xrange(len(pattern)):
			currentSymbol = pattern[ci]
			currentSymbolIndex = 'ACGT$'.index(currentSymbol)
			if currentNode.child[currentSymbolIndex] is None:
				#add a new Node
				newNode = self.Node(self.N)
				self.nodes.append(newNode)
				currentNode.child[currentSymbolIndex] = newNode.number
				self.nodes[currentNode.number] = currentNode
				self.N += 1
				if ci == len(pattern)-1:
					self.nodes[currentNode.number].leave[currentSymbolIndex] = 1 # 
				currentNode = newNode
			else:
				if ci == len(pattern)-1:
					self.nodes[currentNode.number].leave[currentSymbolIndex] = 2
				currentNode = self.nodes[currentNode.child[currentSymbolIndex]]
	
	def maximalNonBranchingPaths(self):
		paths = [] #empty list
		for node in self.nodes:
			outgoingEdgeNode = [ child for child in node.child if child is not None]
			outgoingEdgeNodeIndex = [ci for ci,child in enumerate(node.child) if child is not None]
			if len(outgoingEdgeNode) > 1:
				v = node.number
				for w in outgoingEdgeNode:
					"""for each non 1-in-1-out node, we generate ont non-branching paths"""
					nonbranchingpath = []
					nonbranchingpath.append(v)
					nonbranchingpath.append(w)
					"""update outgoingEdgeNode and w"""
					outgoingEdgeNode = [child for child in self.nodes[w].child if child is not None]
					while (len(outgoingEdgeNode)) == 1:
						w = outgoingEdgeNode[0]
						nonbranchingpath.append(w)
						outgoingEdgeNode = [child for child in self.nodes[w].child if child is not None]
					paths.append(nonbranchingpath)
		#print "maximalNonBranchingPaths:",paths
		return paths

	def printSuffixTrie(self):
		nodes = self.nodes
		for node in nodes:
			idxs = [i for i in range(SuffixTrie.radix) if node.child[i] is not None]
			for idx in idxs:
				print "%d->%d:%d" % (node.number,node.child[idx],node.position[idx])

class SuffixTree(object):
	class Node(object):
		def __init__(self,number):
			self.number = number
			self.child = []
			self.edge = []

	def __init__(self,text):
		self.text = text
		self.nodes = {}

	def modifiedSuffixTreeConstruction(self):
		suffixTrie = SuffixTrie(self.text)
		suffixTrie.constructSuffixTrie()
		nonBranchingPaths = suffixTrie.maximalNonBranchingPaths()
		
		for path in nonBranchingPaths:
			firstNode = path[0]
			firstEdgeEndNode = path[1]
			firstEdgeIndex = suffixTrie.nodes[firstNode].child.index(firstEdgeEndNode)
			pos = suffixTrie.nodes[firstNode].position[firstEdgeIndex]
			length = len(path)-1
			lastNode = path[-1]

			if firstNode not in self.nodes:
				self.nodes[firstNode] = SuffixTree.Node(firstNode)
			self.nodes[firstNode].child.append(lastNode)
			self.nodes[firstNode].edge.append((pos,length))
			'''add the leaves'''
			if lastNode not in self.nodes and len( [c for c in suffixTrie.nodes[lastNode].child if c is None ] ) == 5:
				self.nodes[lastNode] = SuffixTree.Node(lastNode)
				self.nodes[lastNode].edge = suffixTrie.nodes[lastNode].position #special format for leave
	
	def printSuffixTree(self):
		for key,node in self.nodes.items():
			if type(node.edge) == int: #leave
				continue
			for edge in node.edge:
				print self.text[edge[0]:edge[0]+edge[1]]
		
def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			patterns = f.read().splitlines()
	else:
		text = 'ATAAATG$'
	obj = SuffixTree(text)
	obj.modifiedSuffixTreeConstruction()
	obj.printSuffixTree()


if __name__ == '__main__':
	main()
