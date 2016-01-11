#Chunyu Zhao 20151128
import sys

class Trie(object):
	radix = 5 
	''' R-way Trie Node'''
	class Node(object):
		def __init__(self,number):
			self.number = number
			self.child = [None]*Trie.radix
			self.leave = [0]*Trie.radix

	def __init__(self,patterns):
		self.nodes = [self.Node(0)]
		self.N = 1 #number of nodes in Trie
		self.patterns = patterns

	def constructTrie(self):
		for pattern in self.patterns:
			self.put(pattern)

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

	def printTrie(self):
		nodes = self.nodes
		for node in nodes:
			idxs = [i for i in range(Trie.radix) if node.child[i] is not None]
			for idx in idxs:
				print "%d->%d:%s" % (node.number,node.child[idx],'ACGT$'[idx])

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			patterns = f.read().splitlines()
	else:
		patterns = ['ATAGA','ATA','ATGC','GAT']

	trieObj = Trie(patterns)
	trieObj.constructTrie()
	trieObj.printTrie()

if __name__ == '__main__':
	main()
