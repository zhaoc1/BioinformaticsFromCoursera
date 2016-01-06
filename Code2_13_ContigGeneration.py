"""
Contig Generation Problem: Generate the contigs from a collection of reads (with imperfect coverage).
     Input: A collection of k-mers Patterns. 
     Output: All contigs in DeBruijn(Patterns).
"""
#Chunyu Zhao 20150907

import sys, Code2_12_MaximalNonBranchingPaths as maxpath, Code2_5_DeGruijnGraphFromkmers2 as degraph

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		kmers = lines
	else:
		kmers = ['ATG','ATG','TGT','TGG','CAT','GGA','GAT','AGA']

	adjlist,nodes = degraph.build_deGruijnGraphFromKmers(kmers)
	print "number of nodes:",len(nodes)
	numedge = 0
	for v in adjlist.keys():
		numedge += len(adjlist[v])
	print "number of outgoing edges:",numedge
	maxpath = maxpath.maximalNonBranchingPaths(adjlist)
	print "number of contigs",len(maxpath)
	