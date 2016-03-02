__author__ = "Chunyu Zhao"
__copyright__ = "20160301"
import sys
from collections import OrderedDict
from itertools import product

def hmmParameterEstimation(observations,symbols,hiddenpath,states):
	startprobtransition = 1.0/len(states)
	startprobemission = 1.0 / len(symbols)
	emissionCombo =  [''.join(combo) for combo in product(states,symbols)]
	transitionCombo =  [''.join(combo) for combo in product(states, repeat=2)]

	transition = OrderedDict()
	emission = OrderedDict()
	for i in range(len(states)):
		transition[states[i]] = [startprobtransition]*len(states)# initialize with equal probability
		emission[states[i]] = [startprobemission]*len(symbols)
	
	for i in range(len(transitionCombo)):
		edge = transitionCombo[i]
		# count the specific edge
		if edge[0] == hiddenpath[-1] and hiddenpath[:-1].count(edge[0]) != 0:
			transition[edge[0]][states.index(edge[1])] = float(overlappingCount(hiddenpath,edge)) / hiddenpath[:-1].count(edge[0])
		elif hiddenpath.count(edge[0]) != 0:
			transition[edge[0]][states.index(edge[1])] = float(overlappingCount(hiddenpath,edge)) / hiddenpath.count(edge[0])
	
	stateAndstring = [''.join(ss) for ss in zip(hiddenpath,observations)]
	
	for i in range(len(emissionCombo)):
		edge = emissionCombo[i]
		if hiddenpath.count(edge[0]) != 0:
			emission[edge[0]][symbols.index(edge[1])] = float(stateAndstring.count(edge)) / hiddenpath.count(edge[0])
	
	return transition,emission

def printtransition(mat,names):
	print "\t".join([''] + names)
	for name,row in mat.items():
		row = map(float,row)
		print name+"\t" + '\t'.join(["%.3f"]*len(row)) % tuple(row)

def printemission(mat,names,symbols):
	print "\t".join(['']+symbols)
	for name,row in mat.items():
		row = map(float,row)
		print name+"\t" + '\t'.join(["%.3f"]*len(row)) % tuple(row)

def overlappingCount(string,sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()

	observations = lines[0]
	symbols = lines[2].split(' ')
	hiddenpath = lines[4]
	states = lines[6].split(' ')
	transition,emission = hmmParameterEstimation(observations,symbols,hiddenpath,states)
	printtransition(transition,states)
	print "--------"
	printemission(emission,states,symbols)

if __name__ == '__main__':
	main()
