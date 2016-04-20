def HIST(L, N = 10, Gmin = 0, Gmax = 100):
	delta = (Gmax - Gmin) / N
	bin = []
	centers = []
	binlengths = []
	k = 0

	while k != N:
		for grade in L:
			if grade >= (Gmin + k*delta) and grade < (Gmin + (k+1) * delta):
				bin.append(grade)
		average = (((Gmin + (k+1) * delta) - (Gmin + k*delta)) / 2) + (Gmin + k*delta)
		centers.append(average)
		binlengths.append(len(bin))
		bin = []
		k += 1

	out = zip(tuple(centers),tuple(binlengths))

	return list(out)