def word_frequency(s):
	import collections
	wordFreq = {}

	L = s.lower()
	L = L.split()
	for i in L:
		if i in wordFreq:
			wordFreq[i] += 1
		else:
			wordFreq[i] = 1
	return collections.OrderedDict(sorted(wordFreq))