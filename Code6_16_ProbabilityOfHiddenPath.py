#Chunyu Zhao 20160226
import sys
from collections import defaultdict

def probabilityofhiddenpath(hiddenPath,states,transition):
	startProbability = dict(zip(states,[1.0/len(states)]*len(states)))
	prob = startProbability[hiddenPath[0]]
	for i in range(len(hiddenPath)-1):
		prob *= transition[hiddenPath[i]][states.index(hiddenPath[i+1])]
	return prob

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	print lines
	
	hiddenPath = lines[0]
	states = lines[2].split(' ')
	transition = defaultdict(list)
	linenum = 5
	for i in range(len(states)):
		line = lines[linenum].split('\t')
		transition[line[0]] = map(float,line[1:])
		linenum += 1

	prob = probabilityofhiddenpath(hiddenPath,states,transition)
	print prob

if __name__ == '__main__':
	main()