def divisors(n):
	"""Find all divisors of n (no remainders)"""
	div=[]
	M=1
	while M < n:
		if n in div:
			M += 1
		else:
			m = M
			M += 1
			if (n % m == 0):
				div.append(m)
	return(div)

#n=int(input("Enter a number to find all divisors: "))
#k=divisors(n)
#print(k)