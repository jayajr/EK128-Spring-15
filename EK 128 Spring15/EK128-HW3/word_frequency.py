def word_frequency(s):
	import collections
	letters = list("abcdefghijklmnopqrstuvwxyz")
	begin = 0
	end = 0
	L=list(s.lower())
	j=len(L)
	m=L[j-1]
	count = 1
	currentWord = []
	wordFreq = {}

	for i in L:
		count += 1
		if count == j:
			if m in letters:
				end += 2
				currentWord = ''.join(L[begin:end])
				if currentWord in wordFreq:
					wordFreq[currentWord] += 1
				else:
					wordFreq[currentWord] = 1
					out = collections.OrderedDict(sorted(wordFreq.items()))
				return(out)
			else:
				end += 1
				currentWord = ''.join(L[begin:end])
				if currentWord in wordFreq:
					wordFreq[currentWord] += 1
				else:
					wordFreq[currentWord] = 1
				out = collections.OrderedDict(sorted(wordFreq.items()))
				return(out)
		else:
			if i in letters:
				end += 1
			else:
				currentWord = ''.join(L[begin:end])
				if currentWord in wordFreq:
					wordFreq[currentWord] += 1
				else:
					wordFreq[currentWord] = 1
				begin = end+1
				end += 1
				