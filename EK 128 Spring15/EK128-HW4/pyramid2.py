def pyramid2(n):
	m = n
	r = (n - 1)
	start = 0
	end = 1
	x = 2
	out = []
	alphabet = list(n * 'abcdefghijklmnopqrstuvwxyz')

	while m:
		L = alphabet[start:end]
		out.append (r*"-")
		out.append (''.join(L))
		if len(L) > 1:
			M = L[:]
			M.pop()
			M = M[::-1]
			out.append (''.join(M))
		out.append (r*"-")
		out.append ("\n")
		m -= 1
		r -= 1
		start = end
		end = start + x
		x += 1

	out = ''.join(out)
	return (out)
