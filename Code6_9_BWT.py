#Chunyu Zhao 20150722
import sys

def BWT(text):
    """Apply Burrs-Wheeler Transform to input string."""	
    matrix = [text[i:] + text[:i] for i in range(len(text))]
    matrix.sort()
    lastColumn = [r[-1] for r in matrix]
    return "".join(lastColumn)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		with open(filename) as f:
			lines = f.read().splitlines()
		text = lines[0]
	else:
		text = "GCGTGCCTGGTCA$"
	lastColumn = BWT(text)
	print lastColumn