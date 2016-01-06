#Chunyu Zhao 20150909

import sys,Code1_8_HammingDistance as hd

def approximatePatternCount(pattern,text,d):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if hd.hamming_distance(text[i:i+len(pattern)],pattern) <= d:
			count += 1
	return count

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		pattern = lines[0]
		text = lines[1]
		d = int(lines[2])
	else:
		pattern = 'TGT'
		text = 'CGTGACAGTGTATGGGCATCTTT'
		d = 1

	count = approximatePatternCount(pattern,text,d)
	print count