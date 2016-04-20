def flatten(*L):
	out = []

	for i in L:
		if isinstance(i, list or tuple) == True:
			for j in i:
				out.append(j)
		else:
			out.append(i)
	return(out)
