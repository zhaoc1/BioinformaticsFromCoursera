#Chunyu Zhao 20151110
import sys
def greedy_sorting(P):
	approxReversalDistance = 0
	for k in range(len(P)):
		if P[k] != k+1 :
			k_sort(P,k+1)
			approxReversalDistance += 1
		if P[k] == -(k+1):
			k_sort(P,k+1)
			approxReversalDistance += 1
	return approxReversalDistance

def k_sort(p,k):
	if abs(p[k-1]) != k:
		loc = [i for i in range(len(p)) if abs(p[i]) == k]
		loc = loc[0]
		p[k-1:loc+1] = p[k-1:loc+1][::-1]
		p[k-1:loc+1] = [ -1*pi for pi in p[k-1:loc+1] ]
	elif p[k-1] == -1*k:
		p[k-1] = -1 * p[k-1]
	return 

def find_break_points(p):
	p = [0] + p + [len(p)+1]
	num = 0
	for i in range(len(p)-1):
		if p[i+1]-p[i] != 1:
			num += 1
	return num

if __name__ == '__main__':
	filename = sys.argv[1]
	with open(filename) as f:
		lines = f.read().splitlines()
	P = lines[0]
	#P = '(-3 +4 +1 +5 -2)'
	P = map(int,P[1:-1].split(' '))
	print greedy_sorting(P)