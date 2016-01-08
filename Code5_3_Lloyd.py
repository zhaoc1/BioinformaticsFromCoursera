#Chunyu Zhao 20151126
import sys, math
from decimal import *
getcontext().prec = 3

class Lloyd():
	def __init__(self,data,k):
		self.data = data
		self.k = k

	def euclideanDistance(self,v,m):
		return math.sqrt(sum([ (i-j)**2 for i,j in zip(v,m) ]))
	
	def centersToCluster(self,point,centers):
		distances = [self.euclideanDistance(point,center) for center in centers ]
		return distances.index(min(distances))

	def centerOfGravity(self,data):
		numOfPoints = len(data)
		center = map(sum,zip(*data))
		return [ c/numOfPoints for c in center ]

	def checkConverge(self,cen1,cen2):
		for i in range(len(cen1)):
			for c in range(len(cen1[i])):
				if Decimal(cen1[i][c]) != Decimal(cen2[i][c]):
					return False
		return True

	def kMeansCluster(self):
		centers = self.data[:self.k]
		
		while True:
			toCenters = []
			for data in self.data:
				toCenters.append(self.centersToCluster(data,centers))
			newCenters = []
			for cluNum in range(self.k):
				newData = []
				for i,c in enumerate(toCenters):
					if c == cluNum:
						newData.append(self.data[i])
				newCenters.append(self.centerOfGravity(newData))
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
		data = []
		for line in lines[1:]:
			data.append(map(float,line.split(' ')))
	else:
		k = 2
		m = 2
		data = [(1.3,1.1),(1.3,0.2),(0.6,2.8),(3.0,3.2),(1.2,0.7),(1.4,1.6),(1.2,1.0),(1.2,1.1),(0.6,1.5),(1.8,2.6),(1.2,1.3),(1.2,1.0),(0.0,1.9)]

	lloyedObj = Lloyd(data,k)
	centers = lloyedObj.kMeansCluster()
	for center in centers:
		print ' '.join(map(str,center))

if __name__ == '__main__':
	main()
