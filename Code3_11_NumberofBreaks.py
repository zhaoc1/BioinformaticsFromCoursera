#Chunyu Zhao 20151110
import sys

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
	#P = '(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)'
	P = map(int,P[1:-1].split(' '))
	print find_break_points(P)