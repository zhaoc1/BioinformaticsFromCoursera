#Chunyu Zhao 20151024

import sys
from itertools import permutations

def limbLength(mat,n,j):
	leaves = range(n)
	leavesLeft = [l for l in leaves if l != j]
	minlen = float("inf")
	for i,k in permutations(leavesLeft,2):
		if i < k:
			lenik = (mat[j][i]+mat[j][k]-mat[i][k]) / 2
			if lenik < minlen:
				minlen = lenik
	return minlen

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		n = int(lines[0])
		j = int(lines[1])
		mat  = []
		for l in lines[2:]:
			mat.append(map(int,l.split()))
	else:
		mat = [[0,13,21,22],[13,0,12,13],[21,12,0,13],[22,13,13,0]]
		n = 4
		j = 1
	print limbLength(mat,n,j)
	
