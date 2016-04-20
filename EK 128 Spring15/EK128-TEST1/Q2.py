def quadsolve(a,b,c):
	import cmath
	import math
	disc = (b**2) - (4*a*c)
	if disc < 0:
		n = (-b + cmath.sqrt(disc)) /(2*a)
		m = (-b - cmath.sqrt(disc)) /(2*a)
	else:
		n = (-b + math.sqrt(disc)) /(2*a)
		m = (-b - math.sqrt(disc)) /(2*a)
	return(n, m)
