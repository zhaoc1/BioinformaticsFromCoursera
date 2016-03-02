#Chunyu Zhao 20160227
import sys, numpy as np
from collections import OrderedDict

def profileHMM(theta,symbols,msa):
	# check for insertions:
	insertnum = [float(col.count('-'))/len(col) for col in zip(*msa)]
	insertedCol = [n for n,i in enumerate(insertnum) if i>theta]
	# match state number
	matchnum = len(insertnum) - len(insertedCol)
	
	names = ['S','I0']
	for i in range(1,matchnum+1):
		for state in ['M','D','I']:
			names.append(state+str(i))
	names.append('E')

	n = 3*(matchnum+1)
	transition = OrderedDict()
	for i in range(n):
		transition[names[i]] = OrderedDict(zip(names,[0.0]*n))
	
	emission = OrderedDict()
	for i in range(n):
		emission[names[i]] = OrderedDict(zip(symbols,[0.0]*len(symbols)))
	
	# feasible transition: (Mi,Di,Ii) -> (Ii,Mi+1,Di+1)
	for seq in msa:
		mi = 0
		for si in range(len(seq)):
			if si == 0:
				if si in insertedCol:
					prevstate = 'I0'
				else:
					prevstate = 'S'

			if si in insertedCol:
				if seq[si] == '-':
					continue
				else:
					currstate = 'I'+str(mi)
			elif seq[si] == '-':
				currstate = 'D'+str(mi+1)
				mi += 1
			else:
				currstate = 'M'+str(mi+1)
				mi += 1
			transition[prevstate][currstate] += 1

			if seq[si] != '-':
				emission[currstate][seq[si]] += 1
			
			prevstate = currstate
		transition[currstate]['E'] += 1
	transition = normalize(transition,names)
	emission = normalize(emission,names)
	return transition,emission,names

def normalize(mat,names):
	ret = []
	for ti in range(len(mat)):
		newrow = mat[names[ti]].values()
		if newrow.count(0) < len(newrow):
			newrow = [row/sum(newrow) for row in newrow]
		ret.append(newrow)
	return ret

def printtransition(mat,names):
	print "\t".join([''] + names)
	for ri,row in enumerate(mat):
		print names[ri]+"\t" + '\t'.join(["%.3f"]*len(row)) % tuple(row)

def printemission(mat,names,symbols):
	print "\t".join(['']+symbols)
	for ri,row in enumerate(mat):
		print names[ri]+"\t" + '\t'.join(["%.3f"]*len(row)) % tuple(row)


def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	theta = float(lines[0])
	symbols = lines[2].split('\t')#
	msa = []
	for i in range(4,len(lines)):#
		msa.append(lines[i])
	
	transition,emission,names = profileHMM(theta, symbols,msa)
	printtransition(transition,names)
	print "--------"
	printemission(emission,names,symbols)


if __name__ == '__main__':
	main()

