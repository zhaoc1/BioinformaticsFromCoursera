#Chunyu Zhao 20151128
import sys
from TrieConstruction import Trie

def trieMatching(text,patterns):
	trie = Trie(patterns)
	trie.constructTrie()

	result = {}
	for pos in xrange(len(text)):
		ret = prefixTrieMatching(text[pos:],trie)
		if len(ret[0]):
			result[pos] = ret
	return result

def prefixTrieMatching(text,trie):
	pos = 0 #first letter of text
	currentSymbol = text[pos]
	v = 0 #root of the trie
	mapping = 'ACGT$'
	path = []
	pattern = []
	ret = []
	while pos<len(text):
		currentNode = trie.nodes[v]
		idx = 'ACGT$'.index(currentSymbol)
		if currentNode.child[idx] is not None:
			path.append(v) #node path
			pattern.append(currentSymbol) #the pattern by the path from root to v
			if currentNode.leave[idx] == 1:
				#at the last edge, next node is the leave with no outdegree. no need to go there
				ret.append(''.join(pattern))
				return ret
			if currentNode.leave[idx] == 2:
				#the end of sub-pattern, need to continue for longer pattern search
				ret.append(''.join(pattern))
			pos += 1
			if pos != len(text):
				currentSymbol = text[pos]
				v = currentNode.child[idx]
			else:
				if not ret: ret.append([])
				return ret
		else:
			#no matches found
			ret.append([])
			return ret

def main():
	if len(sys.argv) == 2:
		patternfile = sys.argv[1]
		with open(patternfile) as f:
			lines = f.read().splitlines()
		text = lines[0]
		patterns = lines[1:]
	else:
		text = 'AATCGGGTTCAATCGGGGT'
		patterns = ['ATCG','GGGT']
	result = trieMatching(text,patterns)
	print ' '.join(map(str,sorted(result.keys())))
	    
if __name__ == '__main__':
	main()