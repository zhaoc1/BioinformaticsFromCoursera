#Chunyu Zhao 20151109
'''NOT YET! 
since I will have an interview next week, I will leave this question...
but i do have a basic concept about this question: to calculate the second round
of middle point, we use the 0,middleNode,0,middleNode solved by fromSource
and the other half middleNode,n,middleNode,m will be solved by ToSink by reverse
the sequences.
The Key Concept is: once we know the start of the alignment, then we can calcuate 
the columns with gap-filled-first-column.
'''
import sys,math

def getBLOSUM62():
	with open('BLOSUM62.txt', 'r') as f:
		lines = f.read().splitlines()
	alpha = lines[0].lstrip().split()
	blosum62 = []
	for i in range(1,len(lines)):
		blosum62.append(map(int,lines[i][1:].lstrip().split()))
	return blosum62,alpha

def linear_space_alignment(top,bottom,left,right):
	if left == right:
		print 'gap for the second sequence'
		return ['-']*len(top-bottom)
	if top == bottom:
		print 'gap for the first sequence'
		return ['-']*len(right-left)
	middle_node_j = int(math.floor((left+right)/2.0))
	middle_node_i,middle_edge = middle_edge(top,bottom,left,right)
	linear_space_alignment(v,w,top,middle_node_i,left,middle_node_j)
	middle_node_j += 1
	if middle_edge == 1:
		#diagnol
		middle_node_i += 1
	linear_space_alignment(middle_node_i,bottom,middle_node_j,right)

def middle_edge(top,bottom,left,right):
	blosum62,alphabet = getBLOSUM62()
	middle_col = int(math.floor((left+right)/2.0))

	firstCol = range(0,-indel*n,-indel)
	colCount = 1
	while colCount <= middle_col+1:
		nextCol = [None] * n
		nextCol[0] = -indel * colCount
		for i in range(1,n):
			distDiag = firstCol[i-1] + blosum62[alphabet.index(v[i-1])][alphabet.index(w[colCount-1])]
			distHor = firstCol[i] - indel
			distVer = nextCol[i-1] - indel
			candi = [distVer,distHor,distDiag]
			nextCol[i] = max(candi)
		firstCol = nextCol
		if colCount == middle_col:
			middle_row = max([i for i in range(len(nextCol)) if nextCol[i] == max(nextCol)])
		colCount += 1
	for middle_row in middle_rows:
		if nextCol[middle_row+1] >= nextCol[middle_row]:
			middle_edge = 1
		else:
			middle_edge = 2
	return middle_row,middle_edge

if __name__ == '__main__':
	'''filename = sys.argv[1]
	with open(filename) as f:
		str1 = f.readline().strip()
		str2 = f.readline().strip()
	'''
	str1 = 'PLEASANTLY'
	str2 = 'MEANLY'
	indel = 5
	print linear_space_alignment(str1,str2,indel)
