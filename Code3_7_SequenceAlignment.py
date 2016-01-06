import sys,Code3_6_LocalAlignment as local,Code3_5_GlobalAlignment as glob
#Chunyu Zhao 20151031

''' Problem 1: edit distance'''
def edit_distance(x,y,indel=1):
	"down:1, right2: diagnoal:3"
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
			distDiag = D[i-1][j-1] + 1 if x[i-1]==y[j-1] else D[i-1][j-1] - indel
			candi = [distDiag,distVer,distHor]
			D[i][j] = max(candi)
			direction = candi.index(D[i][j])
			'''preference: diag, down, right'''
			if direction == 0:
				pointer[i][j] = 3#diag
			elif direction == 1:
				pointer[i][j] = 1#down
			else:
				pointer[i][j] = 2#right
	return abs(D[-1][-1])

''' Problem 2: fitting alignment '''
def fitting_alignment(x,y,indel=1):
	D = []
	pointer = []
	for i in range(len(x)+1):
		D.append([0]*(len(y)+1))
		pointer.append([None]*(len(y)+1))
	# initialize the first column
	for i in range(len(y)+1,len(x)+1):
		D[i][0] = 0 
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
			distDiag = D[i-1][j-1]+1 if x[i-1]==y[j-1] else D[i-1][j-1] - indel
			candi = [distDiag,distVer,distHor]
			D[i][j] = max(candi)
			direction = candi.index(D[i][j])
			#preference: diag, down, right
			if direction == 1:
				pointer[i][j] = 1#down
			elif direction == 2:
				pointer[i][j] = 2#right
			else:
				pointer[i][j] = 3#diag
	#trace back
	ret = [[],[]]
	lastDCol = zip(*D)[-1]
	lastPointCol = zip(*pointer)[-1]
	indexdiag = [k for k in range(len(lastDCol)) if lastPointCol[k]==3 and k > len(y)]
	lastCol = [lastDCol[ind] for ind in indexdiag]
	i = indexdiag[lastCol.index(max(lastCol))]
	j = len(y)
	score = D[i][j]
	while i != 0 and j!=0:
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
	aln1 = ''.join(ret[0][::-1])
	aln2 = ''.join(ret[1][::-1])
	return score,aln1,aln2

''' Problem 3: overlap alignment '''
def overlap_alignment(x,y,indel=2):
	D = []
	pointer = []
	for i in range(len(x)+1):
		D.append([0]*(len(y)+1))
		pointer.append([None]*(len(y)+1))
	# initialize the first column
	for i in range(len(y)+1,len(x)+1):
		D[i][0] = D[i-1][0] - indel
		pointer[i][0] = 1
	# initialize the first row
	for j in range(1,len(y)+1):
		D[0][j] = 0
		pointer[0][j] = 2

	# fill in the distance matrix and keep the pointer
	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			distHor = D[i][j-1] - indel
			distVer = D[i-1][j] - indel
			distDiag = D[i-1][j-1]+1 if x[i-1]==y[j-1] else D[i-1][j-1] - indel
			candi = [distDiag,distVer,distHor]
			D[i][j] = max(candi)
			direction = candi.index(D[i][j])
			#preference: diag, down, right
			if direction == 1:
				pointer[i][j] = 1#down
			elif direction == 2:
				pointer[i][j] = 2#right
			else:
				pointer[i][j] = 3#diag
	return local.back_track(D,pointer,x,y)

if __name__ == '__main__':
	#filename = sys.argv[1]
	#with open(filename) as f:
	#	str1 = f.readline().strip()
	#	str2 = f.readline().strip()
	#str1 = 'PLEASANTLY'
	#str2 = 'MEANLY'
	#print edit_distance(str1,str2)
	#str1 = 'GTAGGCTTAAGGTTA'
	#str2 = 'TAGATA'
	#score,aln1,aln2 = fitting_alignment(str1,str2)
 	#print '\n'.join([str(score),aln1,aln2])
 	#str1 = 'PAWHEAE'
	#str2 = 'HEAGAWGHEE'
	#indel = 2
	#score,aln1,aln2 = overlap_alignment(str1,str2)
 	#print '\n'.join([str(score),aln1,aln2])
 	str1 = 'GTTGGATTACGAATCGATATCTGTTTG'
 	str2 = 'ACGTCG'
 	print fitting_alignment(str1,str2)
 	str1 = 'AGTT-ACATACTAACG'
 	str2 = 'AGTTCACAGGCTA-CG'
 	score = 0
 	for si in range(len(str1)):
 		if str1[si] == '-' or str2[si] == '-':
 			score -= 2 #indel
 		elif str1[si] == str2[si]:
 			score += 1 #match
 		else:
 			score -= 0 #mismatch
 	print "score:",score

