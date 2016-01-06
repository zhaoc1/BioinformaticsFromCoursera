import sys
#Chunyu Zhao 20151031

def getBLOSUM62():
	with open('data/BLOSUM62.txt', 'r') as f:
		lines = f.read().splitlines()
	alpha = lines[0].lstrip().split()
	blosum62 = []
	for i in range(1,len(lines)):
		blosum62.append(map(int,lines[i][1:].lstrip().split()))
	return blosum62,alpha

def global_alignment(x,y,indel):
	"down:1, right2: diagnoal:3"
	blosum62,alphabet = getBLOSUM62()
	# create the distance matrix
	D = []
	pointer = []
	for i in range(len(x)+1):
		D.append([0]*(len(y)+1))
		pointer.append([None]*(len(y)+1))
	# initialize the first column
	for i in range(1,len(x)+1):
		D[i][0] = D[i-1][0] - indel
		pointer[i][0] = 1
	# initialize the first row
	for j in range(1,len(y)+1):
		D[0][j] = D[0][j-1] - indel
		pointer[0][j] = 2

	# fill in the distance matrix and keep the pointer
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			distHor = D[i][j-1] - indel
			distVer = D[i-1][j] - indel
			distDiag = D[i-1][j-1] + blosum62[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
			candi = [distVer,distHor,distDiag]
			D[i][j] = max(candi)
			direction = candi.index(D[i][j])
			'''preference: diag, down, right'''
			if direction == 2:
				pointer[i][j] = 3#diag
			elif direction == 0:
				pointer[i][j] = 1#down
			else:
				pointer[i][j] = 2#right
	return D[-1][-1],pointer

def back_track(pointer,x,y):
	ret = [[],[]]
	m = len(x)
	n = len(y)
	i = m
	j = n
	while i != 0 and j != 0:
		if pointer[i][j] == 3:
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
	if i == 0:
		ret[1].append(y[:j][::-1])
		ret[0].append('-'*j)
	elif j ==0:
		ret[0].append(x[:i][::-1])
		ret[1].append('-'*i)
	return ''.join(ret[0][::-1]),''.join(ret[1][::-1])

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			str1 = f.readline().strip()
			str2 = f.readline().strip()
	else:
		str1 = 'PLEASANTLY'
		str2 = 'MEANLY' 

	indel = 5
	score,pointer = global_alignment(str1,str2,indel)
	aln1,aln2 = back_track(pointer,str1,str2)
	print '\n'.join([str(score),aln1,aln2])
