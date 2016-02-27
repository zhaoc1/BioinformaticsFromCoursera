#Chunyu Zhao
import sys
from collections import defaultdict

def viterbialgorithm(observations, symbols,states,transition, emission):
	startProbability = dict(zip(states,[1.0/len(states)]*len(states)))
	
	V = [{}]
	edges = [{}]
	for state in states:
		V[0][state] = startProbability[state] * emission[state][symbols.index(observations[0])]
		edges[0][state] = 0 #source
	
	for t in range(1,len(observations)):
		V.append({})
		edges.append({})
		for y in states:
			(prob,state) = max( (V[t-1][y0] * transition[y0][states.index(y)] * emission[y][symbols.index(observations[t])],y0) for y0 in states )
			V[t][y] = prob
			edges[t][y] = state
	
	# BACKTRACK
	opthiddenpath = []
	for x,y in V[-1].items():
		if V[-1][x] == max(V[-1].values()):
			opthiddenpath.append(x)
	for t in range(len(observations)-1,0,-1):
		x = edges[t][x]
		opthiddenpath.append(x)
	print ''.join(opthiddenpath[::-1])# optimal hidden pathway'''

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()

	observations = lines[0]
	symbols = lines[2].split(' ')
	states = lines[4].split(' ')

	transition = defaultdict(list)
	emission = defaultdict(list)
	linenum = 7
	for i in range(len(states)):
		line = lines[linenum].split('\t')
		transition[line[0]] = map(float,line[1:])
		linenum += 1
	
	linenum += 2
	for i in range(len(states)):
		line = lines[linenum].split('\t')
		emission[line[0]] = map(float,line[1:])
		linenum += 1

	viterbialgorithm(observations, symbols,states,transition,emission)

if __name__ == '__main__':
	main()
