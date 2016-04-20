def partition(L,p):
	gtp = []
	etp = []
	ltp = []
	count = 0

	for i in L:
		if i > p:
			gtp.append(i)
		if i == p:
			etp.append(i)
			count += 1
		if i < p:
			ltp.append(i)
	return ltp, count, gtp