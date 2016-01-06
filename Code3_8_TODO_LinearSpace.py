import sys,math
#Chunyu Zhao 20151109
#Not Finished Yet...

def getBLOSUM62():
	with open('BLOSUM62.txt', 'r') as f:
		lines = f.read().splitlines()
	alpha = lines[0].lstrip().split()
	blosum62 = []
	for i in range(1,len(lines)):
		blosum62.append(map(int,lines[i][1:].lstrip().split()))
	return blosum62,alpha

def middle_node(v,w,indel):
	'''FromSource(i)'''
	#from column 0 to collumn middle
	(midNode_i,midNode_j,fromSource) = from_source(v,w,indel)
	''' ToSink(i) '''
	v_rev = v[::-1]
	w_rev = w[::-1]
	(toSink,toSinkMax,) = to_sink(v_rev,w_rev,indel,midNode_j,midNode_i)
	length = fromSource + toSink
	print "middle node: (",midNode_i,",",midNode_j,"),with value:",length,fromSource

	print middle_edge(v,w,indel)

def middle_edge(v,w,indel):
	n = len(v)+1
	blosum62,alphabet = getBLOSUM62()
	middle_col = int(math.floor(len(w)/2.0))
	
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
			middle_rows = [i for i in range(len(nextCol)) if nextCol[i] == max(nextCol)]
			middle_value = max(nextCol)
		colCount += 1
	middle_next = []
	for middle_row in middle_rows:
		if nextCol[middle_row+1] >= nextCol[middle_row]:
			end_i = middle_row+1
			end_j = middle_col+1
		else:
			end_i = middle_row
			end_j = middle_col
		middle_next.append((end_i,end_j))
	return (middle_rows,middle_col,middle_value,middle_next)

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

def to_sink(v,w,indel,middle,i):
	n = len(v)
	m = len(w)
	blosum62,alphabet = getBLOSUM62()
	middle_rev = m - middle
	i_rev = n - i
	firstCol = range(0,-indel*n,-indel)
	colCount = 1
	while colCount <= middle_rev:
		nextCol = [None] * n
		nextCol[0] = -indel * colCount
		for i in range(1,n):
			distDiag = firstCol[i-1] + blosum62[alphabet.index(v[i-1])][alphabet.index(w[colCount-1])]
			distHor = firstCol[i] - indel
			distVer = nextCol[i-1] - indel
			candi = [distVer,distHor,distDiag]
			nextCol[i] = max(candi)
			direction = candi.index(nextCol[i])
		firstCol = nextCol
		colCount += 1
	middle_row = nextCol.index(max(nextCol))
	return (nextCol[i_rev],max(nextCol))

def from_source(v,w,indel):
	n = len(v)+1
	blosum62,alphabet = getBLOSUM62()
	middle = int(math.floor(len(w)/2.0))
	
	firstCol = range(0,-indel*n,-indel)
	colCount = 1
	while colCount <= middle:
		nextCol = [None] * n
		nextCol[0] = -indel * colCount
		for i in range(1,n):
			distDiag = firstCol[i-1] + blosum62[alphabet.index(v[i-1])][alphabet.index(w[colCount-1])]
			distHor = firstCol[i] - indel
			distVer = nextCol[i-1] - indel
			candi = [distVer,distHor,distDiag]
			nextCol[i] = max(candi)
		firstCol = nextCol
		colCount += 1
	middle_row = max([i for i in range(len(nextCol)) if nextCol[i] == max(nextCol)])
	return (middle_row,middle,max(nextCol))

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

if __name__ == '__main__':
	'''filename = sys.argv[1]
	with open(filename) as f:
		str1 = f.readline().strip()
		str2 = f.readline().strip()
	'''
	str1 = 'PLEASANTLY'
	str2 = 'MEANLY'
	indel = 5
	print middle_edge(str1,str2,indel)
	#middle_node(str1,str2,indel)str1 = 'PLEASANTLY'
	print linear_space_alignment(str1,str2,indel)

