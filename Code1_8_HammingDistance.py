"""
Hamming Distance Problem: Compute the Hamming distance between two strings.
     Input: Two strings of equal length.
     Output: The Hamming distance between these strings.
"""
import sys
def hamming_distance(str1,str2):
	hd = 0
	if len(str1) != len(str2):
		print "the two strings different length ERROR"
		return None
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			hd += 1
	return hd

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		str1 = lines[0]
		str2= lines[1]
	else:
		str1 = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
		str2 = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'

	hamDis = hamming_distance(str1,str2)
	print hamDis
	