def pack_crayons(crayons, L = 6):
	row = []
	box = []
	count = 0
	reject = 0

	for i in crayons:
		if i > L:
			reject += 1
		else:
			row.append(i)
			box.append(i)
			if sum(row) > L:
				row = []
				count += 1
				row.append(i)
			elif sum(row) == L:
				row = []
				count +=1
			else:
				continue
	if row:
		count += 1

	space = count * L

	if space != 0:
		fraction = sum(box) / space
	if space == 0:
		fraction = 0

	return(count, fraction, reject)
