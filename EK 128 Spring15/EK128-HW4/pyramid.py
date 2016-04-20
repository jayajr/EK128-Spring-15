def pyramid(n):
	m = n
	r = (n - 1)
	start = 0
	end = 1
	x = 2
	alphabet = list(n * 'abcdefghijklmnopqrstuvwxyz')

	while m:
		L = alphabet[start:end]
		if len(L) > 1:
			M = L[:]
			M.pop()
			M = M[::-1]
			print (r*"-",''.join(L), ''.join(M),r*"-",sep='')
		else:
			print (r*"-",''.join(L),r*"-",sep='')
		m -= 1
		r -= 1
		start = end
		end = start + x
		x += 1
