#Chunyu Zhao
import sys
from collections import defaultdict

def outcomeLikelihood(observations, symbols,states,transition, emission):
	startProbability = dict(zip(states,[1.0/len(states)]*len(states)))
	
	forwardProb = [{}]
	for state in states:
		forwardProb[0][state] = startProbability[state] * emission[state][symbols.index(observations[0])]
	
	for t in range(1,len(observations)):
		forwardProb.append({})
		for y in states:
			forwardProb[t][y] = sum( [forwardProb[t-1][y0] * transition[y0][states.index(y)] * emission[y][symbols.index(observations[t])] for y0 in states ])
	print sum(forwardProb[-1].values())

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

	outcomeLikelihood(observations, symbols,states,transition,emission)

if __name__ == '__main__':
	main()

