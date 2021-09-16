
def printallKlength(set, k):

	n = len(set)
	printallKLRec(set, "", n, k)

def printallKLRec(set, prefix, n, k):
	if (k == 0) :
		print(prefix)
		return

	for i in range(n):
		newPrefix = prefix + set[i]
		printallKLRec(set, newPrefix, n, k - 1)


if __name__ == "__main__":
	
	print("1")
	set1 = ['v', 'q']
	k = 2
	printallKlength(set1, k)
	
	print("\n2")
	set2 = ['s', 'd', 'f', 'z']
	k = 1
	printallKlength(set2, k)


