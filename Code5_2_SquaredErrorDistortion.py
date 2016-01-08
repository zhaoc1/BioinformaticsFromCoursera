#Chunyu Zhao 20151125

import sys,math

class SquaredErrorDistortion():
	def __init__(self,data,centers):
		self.data = data
		self.centers = centers

	def euclideanDistance(self,v,m):
		return math.sqrt(sum([ (i-j)**2 for i,j in zip(v,m) ]))
	
	def distanceDataToCenters(self,point,centers):
			distances = [self.euclideanDistance(point,center) for center in centers ]
			return min(distances)

	def SquaredErrorDistortion(self):
		distortions = []
		for data in self.data:
			distortions.append(self.distanceDataToCenters(data,self.centers) ** 2)
		print "MaxDistance:",math.sqrt(max(distortions))
		return sum(distortions)/len(self.data)

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		k,m = map(int,lines[0].split())
		centers = []
		for i in range(1,k+1):
			centers.append(map(float,lines[i].split()))
		data = []
		for line in lines[k+2:]:
			data.append(map(float,line.split(' ')))
	else:
		centers = [(2.31,4.55),(5.96,9.08)]
		data = [(3.42,6.03),(6.23,8.25),(4.76,1.64),(4.47,4.33),(3.95,7.61),(8.93,2.97),(9.74,4.03),(1.73,1.28),(9.72,5.01),(7.27,3.77)]
		
		centers = [(3,5),(5,4)]
		data = [(2,8),(2,5),(6,9),(7,5),(5,2)]

		#centers = [(4,5),(7,4)]
		#data = [(2,6),(4,9),(5,7),(6,5),(8,3)]

	sedObj = SquaredErrorDistortion(data,centers)
	print sedObj.SquaredErrorDistortion()

if __name__ == '__main__':
	main()
