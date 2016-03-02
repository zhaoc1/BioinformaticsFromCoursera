__author__ = "Chunyu Zhao"
__copyright__ = "20160301"

import sys,HMMParameterEstimation as HMMparaest
from collections import defaultdict

def viterbiLearning(j,observations,symbols,states,transition,emission):
	while j > 0:
		hiddenpath =  viterbialgorithm(observations, symbols,states,transition, emission)
		transition,emission = HMMparaest.hmmParameterEstimation(observations,symbols,hiddenpath,states)
		j -= 1
	return transition,emission

def viterbialgorithm(observations,symbols,states,transition, emission):
	startProbability = dict(zip(states,[1.0/len(states)]*len(states)))
	
	V = [{}] # refers to the score matrix in the video
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
	return ''.join(opthiddenpath[::-1])# optimal hidden pathway'''

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()

	j = int(lines[0])
	observations = lines[2]
	symbols = lines[4].split(' ')
	states = lines[6].split(' ')

	transition = defaultdict(list)
	linenum = 9
	for i in range(len(states)):
		line = lines[linenum].split('\t')
		transition[line[0]] = map(float,line[1:])
		linenum += 1
	emission = defaultdict(list)
	linenum += 2
	for i in range(len(states)):
		line = lines[linenum].split('\t')
		emission[line[0]] = map(float,line[1:])
		linenum += 1
	
	transition,emission = viterbiLearning(j,observations,symbols,states,transition,emission)
	HMMparaest.printtransition(transition,states)
	print "--------"
	HMMparaest.printemission(emission,states,symbols)

if __name__ == '__main__':
	main()
