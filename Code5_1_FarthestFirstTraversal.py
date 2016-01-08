#Chunyu Zhao 20151125
import sys, math

class FarthestFirstTravesal:

	def __init__(self,data,k):
		self.data = data
		self.k = k

	def euclideanDistance(self,v,m):
		return math.sqrt(sum([ (i-j)**2 for i,j in zip(v,m) ]))

	def distanceDataToCenters(self,point,centers):
		distances = [self.euclideanDistance(point,center) for center in centers ]
		return min(distances)

	def addNewCenter(self,centers):
		#maxDistanceDatasToCenters
		newCenter = None
		maxLength = float('-inf')
		for point in self.data:
			segmentLen = self.distanceDataToCenters(point,centers)
			if segmentLen > maxLength:
				maxLength = segmentLen
				newCenter = point
		return newCenter

	def fartherFirstTravesal(self):
		centers = [self.data[0]]
		while len(centers) < self.k:
			centers.append(self.addNewCenter(centers))
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
		k = 3
		m = 2
		data = [(0.0,0.0),(5.0,5.0),(0.0,5.0),(1.0,1.0),(2.0,2.0),(3.0,3.0),(1.0,2.0)]
	
	fftObj = FarthestFirstTravesal(data,k)
	fftObj.fartherFirstTravesal()
	centers = fftObj.fartherFirstTravesal()
	for center in centers:
		print ' '.join(map(str,center))

if __name__ == '__main__':
	main()