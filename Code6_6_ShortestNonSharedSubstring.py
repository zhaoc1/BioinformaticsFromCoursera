#Chunyu Zhao
import sys
from LongestRepeats import BreadthFirstPaths
from LongestSharedSubstring import ColoredSuffixTree

def shortestUnsharedSubstring(text):
	suffixTree = ColoredSuffixTree(text)
	suffixTree.modifiedSuffixTreeConstruction()
	suffixTree.treeColoring()
	
	bfpath = BreadthFirstPaths(suffixTree,text)
	bfpath.bfs(0)
	
	shortestLen = float("inf")
	shortestNode = None

	for i in suffixTree.nodes.keys():
		node = suffixTree.nodes[i]
		if node.color != 2 and len(node.child) > 0:
			currentPath =  bfpath.pathTo[i]
			if len(currentPath) < shortestLen:
				shortestNode = i
				shortestLen = len(currentPath)
	print bfpath.pathTo[shortestNode]

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text1 = lines[0] + '#'
		text2 = lines[1] + '$'
	else:
		text1 = 'CCAAGCTGCTAGAGG#'
		text2 = 'CATGCTGGGCTGGCT$'
	text = text1 + text2
	shortestUnsharedSubstring(text)

if __name__ == '__main__':
	main()
