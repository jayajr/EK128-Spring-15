#Uses ASCII value of character as comparison point.
#E.g. '1'=49 'A'=65 'a'=97,
#Therefore 1AaA1 is a hill, aA1Aa is a valley
#An empty string is always False.n
#A hill first strictly ascends then strictly descends.
#A slope never ascends.
#A valley first strictly descends then strictly ascends.

def is_hill(seq):
	diff = []
	index = 0
	index2 = 1
	m = len(seq)
	L= list(seq)

	if seq == "":
		return(False)

	while True:
		if index2 == m:
			break
		x = ord(L[index2]) - ord(L[index])
		diff.append(x)
		index += 1
		index2 += 1

	index = 0
	for i in diff:
		index += 1
		if i <= 0:
			out = False
			break
		if i > 0:
			continue
	for i in diff[index-1:]:
		if i >= 0:
			out = False
			break
		if i < 0:
			out = True
			continue

	return(out)


def is_plain(seq):
	diff = []
	index = 0
	index2 = 1
	m = len(seq)
	L= list(seq)

	if seq == "":
		return(False)

	while True:
		if index2 == m:
			break
		x = ord(L[index2]) - ord(L[index])
		diff.append(x)
		index += 1
		index2 += 1

	for i in diff:
		if i < 0 or i > 0:
			out = False
			break
		if i == 0:
			out = True
			continue

	return(out)


def is_ramp(seq):
	diff = []
	index = 0
	index2 = 1
	m = len(seq)
	L= list(seq)

	if seq == "":
		return(False)

	while True:
		if index2 == m:
			break
		x = ord(L[index2]) - ord(L[index])
		diff.append(x)
		index += 1
		index2 += 1

	for i in diff:
		if i > 0:
			out = True
			continue
		if i <= 0:
			out = False
			break

	return(out)


def is_slope(seq):
	diff = []
	index = 0
	index2 = 1
	m = len(seq)
	L= list(seq)

	if seq == "":
		return(False)

	while True:
		if index2 == m:
			break
		x = ord(L[index2]) - ord(L[index])
		diff.append(x)
		index += 1
		index2 += 1

	for i in diff:
		if i < 0:
			out = True
			continue
		if i >= 0:
			out = False
			break

	return(out)


def is_valley(seq):
	diff = []
	index = 0
	index2 = 1
	m = len(seq)
	L= list(seq)

	if seq == "":
		return(False)

	while True:
		if index2 == m:
			break
		x = ord(L[index2]) - ord(L[index])
		diff.append(x)
		index += 1
		index2 += 1

	index = 0
	for i in diff:
		index += 1
		if i < 0:
			continue
		if i >= 0:
			out = False
			break
	for i in diff[index-1:]:
		if i > 0:
			out = True
			continue
		if i <= 0:
			out = False
			break


	return(out)


def get_topology(seq):
	plain = is_plain(seq)
	slope = is_slope(seq)
	ramp = is_ramp (seq)
	hill = is_hill(seq)
	valley = is_valley(seq)

	if plain is True:
		return("Plain")
	if slope is True:
		return("Slope")
	if ramp is True:
		return("Ramp")
	if hill is True:
		return("Hill")
	if valley is True:
		return("Valley")
	else:
		return("None")
