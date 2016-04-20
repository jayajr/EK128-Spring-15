def quick(L):
	#Useless and not pythonic
	#Could just use sorted()
	#sorted() is better too since mine will not sort floats properly
	p = 0
	sorted_list = []

	while p <= max(L)
		pOut = partition (L, p)
		ltp = pOut[0]
		gtp = pOut[2]

		multiples = pOut[1]
		while multiples != 0:
			sorted_list.append(p)
			multiples -= 1
		p += 1
	return sorted_list
		

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