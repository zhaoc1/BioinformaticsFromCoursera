'''
Output LCS Problem
'''
#Chunyu Zhao
import os
import sys

def interpreter(conn):
    v = conn.readline().strip()
    w = conn.readline().strip()
    return v,w

def lcsBacktrack(v,w):
	"down:1, right2: diagnoal:3"
	n = len(v)
	m = len(w)
	s = []
	backtracking = []
	[s.append([None]*(m+1)) for i in range(n+1)]
	[backtracking.append([None]*(m+1)) for i in range(n+1)]
	s[0][0] = 0 
	for i in range(1,n+1):
		s[i][0] = 0
		backtracking[i][0] = 1 
	for j in range(1,m+1):
		s[0][j] = 0
		backtracking[0][j] = 2
	for i in range(1,n+1):
		for j in range(1,m+1):
			candidate = [s[i-1][j],s[i][j-1],s[i-1][j-1]+1 if v[i-1]==w[j-1] else s[i-1][j-1]]
			s[i][j] = max(candidate)
			'''the ordering of the if-elif actually make differences:diagnonal > down > right'''
			if s[i][j] == s[i-1][j-1]+1 and v[i-1]==w[j-1]:
				backtracking[i][j] = 3
			elif s[i][j] == s[i-1][j]:
				backtracking[i][j] = 1
			elif s[i][j] == s[i][j-1]:
				backtracking[i][j] = 2
	return backtracking

def outputLCS(backtracking,v,i,j):
	global lcs
	if i == 0 or j == 0 :
		return
	if backtracking[i][j] == 1:
		outputLCS(backtracking,v,i-1,j)
	elif backtracking[i][j] == 2:
		outputLCS(backtracking,v,i,j-1)
	else:
		outputLCS(backtracking,v,i-1,j-1)
		lcs.append(v[i-1])

if __name__ == '__main__':
	v = 'AACCTTGG'
	w = 'ACACTGTGA'
	global lcs
	lcs = []
	sys.setrecursionlimit(2000)
	backtracking = lcsBacktrack(v,w)
	outputLCS(backtracking,v,len(v),len(w))
	print ''.join(lcs)