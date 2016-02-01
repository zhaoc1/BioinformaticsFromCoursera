#Chunyu Zhao 20151128,20160201

import sys
from collections import defaultdict
from LongestRepeats import BreadthFirstPaths

class ColoredSuffixTrie(object):
	radix = 6
	class Node(object):
		def __init__(self,number):
			self.number = number
			self.child = [None]*ColoredSuffixTrie.radix
			self.position = [None]*ColoredSuffixTrie.radix
			self.color = None #colormap = {'red': 0, 'blue':1, 'purple': 2}

	def __init__(self,text):
		self.nodes = [self.Node(0)]
		self.N = 1 #number of nodes in Trie
		self.text = text
		self.half = text.index('#')

	def constructSuffixTrie(self):
		for i in xrange(len(self.text)):
			currentNode = self.nodes[0] #root
			for j in xrange(i,len(self.text)):
				currentSymbol = self.text[j]
				currentSymbolIndex = 'ACGT#$'.index(currentSymbol)
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
				# leave
				currentNode.position = i
				if i < self.half:
					currentNode.color = 0
				else:
					currentNode.color = 1
				self.nodes[currentNode.number] = currentNode

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
		return paths

	def printSuffixTrie(self):
		nodes = self.nodes
		for node in nodes:
			idxs = [i for i in range(SuffixTrie.radix) if node.child[i] is not None]
			for idx in idxs:
				print "%d->%d:%d" % (node.number,node.child[idx],node.position[idx])

class ColoredSuffixTree(object):
	class Node(object):
		def __init__(self,number):
			self.number = number
			self.child = []
			self.edge = []
			self.color = None

	def __init__(self,text):
		self.text = text
		self.nodes = {}

	def modifiedSuffixTreeConstruction(self):
		suffixTrie = ColoredSuffixTrie(self.text)
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
				self.nodes[firstNode] = ColoredSuffixTree.Node(firstNode)
			self.nodes[firstNode].child.append(lastNode)
			self.nodes[firstNode].edge.append((pos,length))
			'''add the leaves'''
			if lastNode not in self.nodes and len( [c for c in suffixTrie.nodes[lastNode].child if c is None ] ) == 6:
				self.nodes[lastNode] = ColoredSuffixTree.Node(lastNode)
				self.nodes[lastNode].edge = suffixTrie.nodes[lastNode].position #special format for leave
				self.nodes[lastNode].color = suffixTrie.nodes[lastNode].color
	
	def treeColoring(self):
		colorlessNode = [node for node in self.nodes.keys() if self.nodes[node].color is None]
		while len(colorlessNode) > 0:
			self.findRipenodes()
			colorlessNode = [node for node in self.nodes.keys() if self.nodes[node].color is None]
	
	def findRipenodes(self):
		for node in self.nodes.keys():
			if self.nodes[node].color is None:
				children = self.nodes[node].child
				coloredChildren = [c for c in children if self.nodes[c].color is not None]
				childrenColor = [self.nodes[c].color for c in children if self.nodes[c].color is not None]
				if len(coloredChildren) == len(children) and len(children)>0:
					if childrenColor.count(childrenColor[0]) != len(childrenColor):
						self.nodes[node].color = 2
					else:
						self.nodes[node].color = childrenColor[0]

def longestSharedSubstring(text):
	suffixTree = ColoredSuffixTree(text)
	suffixTree.modifiedSuffixTreeConstruction()
	suffixTree.treeColoring()
	bfpath = BreadthFirstPaths(suffixTree,text)
	bfpath.bfs(0)
	longestSubstring = ''
	for i in suffixTree.nodes.keys():
		node = suffixTree.nodes[i]
		if node.color == 2 and len(node.child) > 0:
			currentPath =  bfpath.pathTo[i]
			if len(currentPath) > len(longestSubstring):
				longestSubstring = currentPath
	print longestSubstring

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text1 = lines[0] + '#'
		text2 = lines[1] + '$'
	else:
		text1 = 'TCGGTAGATTGCGCCCACTC#'
		text2 = 'AGGGGCTCGCAGTGTAAGAA$'
	
	text = text1 + text2
	longestSharedSubstring(text)

if __name__ == '__main__':
	main()
