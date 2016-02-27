#Chunyu Zhao 20160226
import sys
from collections import defaultdict

def probabilityofoutcomegivenpath(observations, symbols, hiddenPath,states,emission):
	prob = 1
	for i in range(len(hiddenPath)):
		prob *= emission[hiddenPath[i]][symbols.index(observations[i])]
	return prob

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	print lines
	
	observations = lines[0]
	symbols = lines[2].split(' ')
	hiddenPath = lines[4]
	states = lines[6].split(' ')

	emission = defaultdict(list)
	linenum = 9
	for i in range(len(states)):
		line = lines[linenum].split('\t')
		print line
		emission[line[0]] = map(float,line[1:])
		linenum += 1
	
	prob = probabilityofoutcomegivenpath(observations,symbols,hiddenPath,states,emission)
	print prob

if __name__ == '__main__':
	main()