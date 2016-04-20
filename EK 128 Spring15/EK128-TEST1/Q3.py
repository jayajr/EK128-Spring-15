def altsum(L):
	count = -1
	M = []
	for i in L:
		count += 1
		if (count % 2 == 0):
			M.append(i)
		else:
			i = -i
			M.append(i)
	out = sum(M)
	return(out)
