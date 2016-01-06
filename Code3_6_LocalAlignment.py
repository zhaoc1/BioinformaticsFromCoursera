import sys
#Chunyu Zhao

def getScore():
	with open('data/PAM250_1.txt', 'r') as f:
		lines = f.read().splitlines()
	alphabet = lines[0].lstrip().split()
	score = []
	for i in range(1,len(lines)):
		score.append(map(int,lines[i][1:].lstrip().split()))
	return score,alphabet

def local_alignment(x,y,indel):
	"down:1, right2: diagnoal:3"
	score,alphabet = getScore()
	# create the distance matrix
	D = []
	pointer = []
	for i in range(len(x)+1):
		D.append([0]*(len(y)+1))
		pointer.append([-1]*(len(y)+1))

	# fill in the distance matrix and keep the pointer
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			distHor = D[i][j-1] - indel
			distVer = D[i-1][j] - indel
			distDiag = D[i-1][j-1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
			candi = [0,distVer,distHor,distDiag]
			D[i][j] = max(candi)
			direction = candi.index(D[i][j])
			'''preference: diag, down, right'''
			if direction == 0:
				pointer[i][j] = -1 #STOP
			elif direction == 1:
				pointer[i][j] = 1#down
			elif direction == 2:
				pointer[i][j] = 2#right
			elif direction == 3:
				pointer[i][j] = 3#diag
	return D,pointer

def back_track(D,pointer,x,y):
	ret = [[],[]]
	maxrow = [max(row) for row in D]
	maxcol = [max(col) for col in zip(*D)]
	maxscore = max(maxcol)
	i = maxrow.index(maxscore)
	j = maxcol.index(maxscore)
	while i != 0 and j != 0:
		if pointer[i][j] == -1:
			break
		elif pointer[i][j] == 3:
			ret[0].append(x[i-1])
			ret[1].append(y[j-1])
			i -= 1
			j -= 1
		elif pointer[i][j]== 1:
			ret[0].append(x[i-1])
			ret[1].append('-')
			i -= 1
		else:
			ret[0].append('-')
			ret[1].append(y[j-1])
			j -=1
	return maxscore,''.join(ret[0][::-1]),''.join(ret[1][::-1])

if __name__ == '__main__':
	filename = sys.argv[1]
	with open(filename) as f:
		str1 = f.readline().strip()
		str2 = f.readline().strip()
	indel = 5
	score,pointer = local_alignment(str1,str2,indel)
	maxscore,aln1,aln2 = back_track(score,pointer,str1,str2)
	print '\n'.join([str(maxscore),aln1,aln2])
