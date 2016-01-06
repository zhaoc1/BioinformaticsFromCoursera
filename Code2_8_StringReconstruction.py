"""
CODE CHALLENGE: Solve the String Reconstruction Problem.
     Input: An integer k followed by a list of k-mers Patterns.
     Output: A string Text with k-mer composition equal to Patterns. 
     (If multiple answers exist, you may return any one.)
"""
#Chunyu Zhao 20150910
import sys, Code2_5_DeGruijnGraphFromkmers2 as degraph, Code2_7_EulerianPath as eupath

if len(sys.argv) == 2:
	filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	kmers = lines
else:
	k = 4
	kmers = ['CTTA','ACCA','TACC','GGCT','GCTT','TTAC']


adjlist,nodes = degraph.build_deGruijnGraphFromKmers(kmers)
path = eupath.eulerian_path(adjlist)
epath = [nodes[p] for p in path]
string = [epath[0]]
for pa in epath[1:]:
	string.append(pa[-1])
print ''.join(string)
