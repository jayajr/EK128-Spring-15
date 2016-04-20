def get_digits(n,d):
	rmdrs = [] 
	allrmdrs = []
	quot = []
	no_repeat = []

	index = 0
	rem = n
	rem = rem / 10

	while len(rmdrs) == len(allrmdrs):
		rem = rem * 10
		dig = int(rem // d)
		rem = (rem % d)
		allrmdrs.append(rem)
		quot.append(dig)

		if rem not in rmdrs:
			rmdrs.append(rem)

		if rem == 0:
			no_repeat = quot
			break

	if quot[0] == 0:
		del quot[0]

	for i in rmdrs:
		if rmdrs[index] == rem:
			x = index
		index += 1
	while x != 0:
		no_repeat.append(quot[x-1])
		del quot[x-1]
		x -= 1
	if rem == 0:
		return(list(quot[::-1]),[])
	else:
		return(list(no_repeat[::-1]), list(quot))
