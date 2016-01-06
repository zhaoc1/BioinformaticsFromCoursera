"""
 StringSpelledByGappedPatterns(GappedPatterns, k, d)
        FirstPatterns <- the sequence of initial k-mers from GappedPatterns
        SecondPatterns <- the sequence of terminal k-mers from GappedPatterns
        PrefixString <- StringSpelledByPatterns(FirstPatterns, k)
        SuffixString <- StringSpelledByPatterns(SecondPatterns, k)
        for i = k + d + 1 to |PrefixString|
            if the i-th symbol in PrefixString does not equal the (i - k - d)-th symbol in SuffixString
                return "there is no string spelled by the gapped patterns"
        return PrefixString concatenated with the last k + d symbols of SuffixString
""" 
#Chunyu Zhao 20150907

import sys, Code2_7_EulerianPath as eupath

def stringSpelledByGappedPatterns(gappedPatterns, k, d):
	firstPatterns = [ pat.split('|')[0] for pat in gappedPatterns ]
	secondPatterns = [ pat.split('|')[1].rstrip() for pat in gappedPatterns ]
	preffixString = stringSpelledByPatterns(firstPatterns,k)
	suffixString = stringSpelledByPatterns(secondPatterns,k)
	if preffixString[k+d:] == preffixString[k+d:]:
		return preffixString + suffixString[-k-d:]
	else:
		return None

def stringSpelledByPatterns(patterns,k):
	string = [patterns[0]]
	for pat in patterns[1:]:
		string.append(pat[-1])
	return ''.join(string)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		k = int(lines[0].split()[0])
		d = int(lines[0].split()[1])
		gappedPatterns = lines[1:]
	else:
		gappedPatterns = ['GACC|GCGC','ACCG|CGCC','CCGA|GCCG','CGAG|CCGG','GAGC|CGGA']
		k = 4
		d = 2

	constructedString = stringSpelledByGappedPatterns(gappedPatterns,k,d)
	print constructedString
