#Chunyu Zhao 20151126
import sys, math

class SoftKMeans():
	def __init__(self,data,k,beta):
		self.data = data
		self.k = k
		self.beta = beta

	def euclideanDistance(self,v,w):
		return math.sqrt(sum([ (i-j)**2 for i,j in zip(v,w) ]))

	def dotProduct(self,v,w):
		return sum( v[i]*w[i] for i in range(len(v)))

	def checkConverge(self,cen1,cen2):
		for i in range(len(cen1)):
			if self.euclideanDistance(cen1[i],cen2[i]) > 0.001:
				return False
		return True

	def SoftKMeans(self):
		centers = self.data[:self.k]
		while True:
			#HiddenMatrix: k*n
			hiddenMatrix = []
			for center in centers:
				hiddenVector = [2.72 ** (-self.beta * self.euclideanDistance(point,center)) for point in self.data]
				hiddenMatrix.append(hiddenVector)
			#normalize HiddenMatrix by column
			hiddenMatrixTrans = zip(*hiddenMatrix)
			for col in range(len(hiddenMatrixTrans)):
				colSum = sum(hiddenMatrixTrans[col])
				hiddenMatrixTrans[col] = [ element/colSum for element in hiddenMatrixTrans[col] ]
			hiddenMatrix = zip(*hiddenMatrixTrans)

			dataTrans = zip(*self.data)
			newCenters = []
			for ci in range(self.k):
				s = sum(hiddenMatrix[ci])
				newCenters.append([ self.dotProduct(hiddenMatrix[ci],col)/s for col in dataTrans ])
			
			if self.checkConverge(centers,newCenters):
				break
			else:
				centers = newCenters
		return centers


def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		k,m = map(int,lines[0].split())
		beta = float(lines[1])
		data = []
		for line in lines[2:]:
			data.append(map(float,line.split(' ')))
	else:
		k = 2
		m = 2
		beta = 2.7
		data = [(1.3,1.1),(1.3,0.2),(0.6,2.8),(3.0,3.2),(1.2,0.7),(1.4,1.6),(1.2,1.0),(1.2,1.1),(0.6,1.5),(1.8,2.6),(1.2,1.3),(1.2,1.0),(0.0,1.9)]


	skmObj = SoftKMeans(data,k,beta)
	centers = skmObj.SoftKMeans()
	for center in centers:
		print ' '.join(map(str,center))

if __name__ == '__main__':
	main()

