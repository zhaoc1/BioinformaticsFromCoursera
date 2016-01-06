#Chunyu Zhao 20151119
import sys,copy
from collections import defaultdict

#edgesToCycle took me 2 days... instead of based on nodes,
#we should really based on edges directly!!! FirstTimeLearning!!

def colored_edges(chromosomes):
	edges = []
	for chromosome in chromosomes:
		nodes = chromosome_cycle(chromosome)
		n = len(nodes)
		for j in range(len(chromosome)):
			edges.append((nodes[(2*j+1)%n], nodes[(2*j+2)%n]))
	return edges

def black_edges(coloredges):
	n = len(coloredges)
	edges = []
	for j in range(1,n+1):
		edges.append((2*j-1,2*j))
	return edges

def chromosome_cycle(chromosome):
	nodes = [0] * len(chromosome)*2
	for j in range(len(chromosome)):
		i = chromosome[j]
		if i > 0:
			nodes[2*j] = 2*i-1
			nodes[2*j+1] = 2*i
		else:
			nodes[2*j] = -2 * i
			nodes[2*j+1] = -2 * i -1
	return nodes

def cycle_chromosome(nodes):
	chromosomes = []
	for node in nodes:
		chromosome = [0] * (len(node)/2)
		for j in range(1,len(node)/2+1):
			if node[2*j-1-1] < node[2*j-1]:
				chromosome[j-1] = node[2*j-1]/2
			else:
				chromosome[j-1] = -node[2*j-1-1]/2
		chromosomes.append(chromosome)
	return chromosomes

def edges_genome(Edge):
	edges = copy.deepcopy(Edge)
	cycles = []
	cycle = []

	(nodei,nodej) = edges[0]
	cycle.append(nodei)
	cycle.append(nodej)
	edges.remove((nodei,nodej))
	while len(edges)>0:
		if nodej % 2 == 0:
			nextEdge = [ edge for edge in edges if nodej-1 in edge]
			linknode = nodej - 1
		else:
			nextEdge =  [ edge for edge in edges if nodej+1 in edge]
			linknode = nodej + 1

		if len(nextEdge) == 0:
			cycles.append(cycle)
			cycle = []
			(nodei,nodej) = edges[0]
			edges.remove((nodei,nodej))
		else:
			if linknode == nextEdge[0][1]:
				(nodej,nodei) = nextEdge[0]
			else:
				(nodei,nodej) = nextEdge[0]
			edges.remove(nextEdge[0])

		cycle.append(nodei)
		cycle.append(nodej)
		
	cycles.append(cycle)
	for ci,cycle in enumerate(cycles):
		#need the shuttle the linear list nto proper order:adjacent black need to be together
		cycles[ci] = cycle[1:]+cycle[:1]
	return cycles

def find_cycles(coloredges,blackedges):
	colcol1 = list(zip(*coloredges)[0])
	colcol2 = list(zip(*coloredges)[1])
	blacol1 = list(zip(*blackedges)[0])
	blacol2 = list(zip(*blackedges)[1])

	n = 2 * len(coloredges)
	''' coloredges are bi-direction, while black edges is uni-directed
	and our task is to determine the direction of the default blackEdges 
	using the information of the undirected color edges'''
	
	cycles = []
	while sum(map(len,cycles)) < n:
		cycle = []
		nodei = blacol1[0]
		while nodei not in cycle:
			if nodei % 2 == 1: #tail
				(nodei, nodej) = [edge for edge in blackedges if nodei in edge][0]
				blacol1.remove(nodei)
				blacol2.remove(nodej)
			else: #head
				(nodej, nodei) = [edge for edge in blackedges if nodei in edge][0]
				blacol1.remove(nodej)
				blacol2.remove(nodei)

			if nodej in colcol1:
				cycle.append(nodei)
				cycle.append(nodej)
				ind = colcol1.index(nodej)
				colcol1.remove(nodej)
				nodei = colcol2[ind]
				colcol2.pop(ind)
			elif nodei in colcol1:
				cycle.append(nodej)
				cycle.append(nodei)
				ind = colcol1.index(nodei)
				colcol1.remove(nodei)
				nodei = colcol2[ind]
				colcol2.pop(ind)
			elif nodej in colcol2:
				cycle.append(nodei)
				cycle.append(nodej)
				ind = colcol2.index(nodej)
				colcol2.remove(nodej)
				nodei = colcol1[ind]
				colcol1.pop(ind)
		cycles.append(cycle)
	return cycles

def red_blue_cycles(rededges,blueedges):
	redcol1 = list(zip(*rededges)[0])
	redcol2 = list(zip(*rededges)[1])
	bluecol1 = list(zip(*blueedges)[0])
	bluecol2 = list(zip(*blueedges)[1])
	cycles = []

	while sum(map(len,cycles)) < 2 * len(rededges):
		cycle = []
		nodei = redcol1[0]
		while nodei not in cycle:
			cycle.append(nodei)
			if nodei in redcol1:
				nodej = redcol2[redcol1.index(nodei)]
				redcol1.remove(nodei)
				redcol2.remove(nodej)
			elif nodei in redcol2:
				nodej = redcol1[redcol2.index(nodei)]
				redcol2.remove(nodei)
				redcol1.remove(nodej)
			cycle.append(nodej)
			if nodej in bluecol1:
				nodei = bluecol2[bluecol1.index(nodej)]
				bluecol1.remove(nodej)
				bluecol2.remove(nodei)
			else:
				nodei = bluecol1[bluecol2.index(nodej)]
				bluecol2.remove(nodej)
				bluecol1.remove(nodei)
		cycles.append(cycle)
	return cycles

def print_p(redcycles):
	P = cycle_chromosome(redcycles)
	printP = []
	for p in P:
		printP.append("(%s)" % ' '.join("%+d" % e for e in p) )
	print ''.join(printP)

def two_break_dist(P,Q): #calcualte the 2-break distance!
	rededges =  colored_edges(P)
	blueedges = colored_edges(Q)
	cycles = red_blue_cycles(rededges,blueedges)
	n = sum(map(len,P))
	return n - len(cycles)

def shortest_rearrangement(P,Q):
	rededges =  colored_edges(P)
	blueedges = colored_edges(Q)

	redcycles = edges_genome(rededges)
	print_p(redcycles)

	cycles = red_blue_cycles(rededges,blueedges)
	n = sum(map(len,P))
	breakDist = n - len(cycles)
	#print "2-break-distance:",breakDist

	while breakDist > 0:
		''' select an arbitrary edge from blueedges: (j1,i2) '''
		found = 0
		for cycle in cycles:
			#print "cycles",cycles
			if len(cycle) == 2:
				continue
			for ci in range(len(cycle)-1):
				if (cycle[ci], cycle[ci+1]) in blueedges:
					found = 1
					(j1,i2) = (cycle[ci], cycle[ci+1])
					break
			if found == 0:
				for ci in range(len(cycle)-1):
					if (cycle[ci+1], cycle[ci]) in blueedges:
						(j1,i2) = (cycle[ci+1], cycle[ci])
						break

		(i1,j1) =  [red for red in rededges if j1 in red][0]
		(i2,j2) = [red for red in rededges if i2 in red][0]

		''' we need to pick the exact 2-breaks that increase the distance! '''
		redtemp1 = copy.deepcopy(rededges)
		redtemp2 = copy.deepcopy(rededges)

		#print "rededges",rededges,i1,j1,i2,j2
		redtemp1.remove((i1,j1))
		redtemp1.remove((i2,j2))
		redtemp1.append((j1,i2))
		redtemp1.append((i1,j2))
		cycles1 = red_blue_cycles(redtemp1,blueedges)
		newbreakDist1 = n - len(cycles1)

		redtemp2.remove((i1,j1))
		redtemp2.remove((i2,j2))
		redtemp2.append((j1,j2))
		redtemp2.append((i1,i2))
		cycles2 = red_blue_cycles(redtemp2,blueedges)
		newbreakDist2 = n - len(cycles2)

		if newbreakDist1  < breakDist:
			breakDist = newbreakDist1
			rededges.remove((i1,j1))
			rededges.remove((i2,j2))
			rededges.append((j1,i2))
			rededges.append((i1,j2))
		elif newbreakDist2 < breakDist:
			breakDist = newbreakDist2
			rededges.remove((i1,j1))
			rededges.remove((i2,j2))
			rededges.append((j1,j2))
			rededges.append((i1,i2))
		else:
			"error!!!"
		
		cycles = red_blue_cycles(rededges,blueedges)
		redcycles = edges_genome(rededges)
		print_p(redcycles)
		newP = cycle_chromosome(redcycles)
		dist = two_break_dist(newP,Q)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		P = lines[0]
		Q = lines[1]
	else:
		P = '(+1 -2 -3 +4)'
		Q = '(+1 +2 -4 -3)'

	P = [map(int,P.strip().lstrip('(').rstrip(')').split(' '))]
	Q = [map(int,Q.strip().lstrip('(').rstrip(')').split(' '))]
	dist = two_break_dist(P, Q)
	print "2-break distance is: ", dist
	shortest_rearrangement(P,Q)
	