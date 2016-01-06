'''
Find a longest path in Manhattan Tourist Problem
'''
#Chunyu Zhao 20151025

import os

def interpreter(conn):
    n, m = map(int,conn.readline().strip().split(' '))
    Down = []
    Right = []
    for _ in range(n):
    	Down.append(map(int,conn.readline().strip().split(' ')))
    conn.readline()
    for _ in range(n+1):
    	Right.append(map(int,conn.readline().strip().split(' ')))
    return n,m,Down,Right

def longest_path(n,m,Down,Right):
	s = []
	[s.append([None]*(m+1)) for i in range(n+1)]
	s[0][0] = 0
	for i in range(1,n+1):
		s[i][0] = s[i-1][0] + Down[i-1][0]
	for j in range(1,m+1):
		s[0][j] = s[0][j-1] + Right[0][j-1]
	for i in range(1,n+1):
		for j in range(1,m+1):
			down = s[i-1][j] + Down[i-1][j]
			right = s[i][j-1] + Right[i][j-1]
			s[i][j] = max(down,right)
	return s[-1][-1]

if __name__ == '__main__':
	os.chdir('/Users/April/Documents/BioinformaticsAlgorithm/3.ComparingGenesProteinsandGenomes/')
	with open('dataset_261_9.txt', 'r') as f:
		n,m,Down,Right = interpreter(f)
	print longest_path(n,m, Down, Right)