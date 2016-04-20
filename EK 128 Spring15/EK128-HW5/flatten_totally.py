def flatten_totally(*L):
	def flatten(L):
		for i in L:
			if isinstance(i, list or tuple) == False:
				yield i
			else:
				for j in flatten(i):
					yield j
	out = list(flatten(L))
	return out
	