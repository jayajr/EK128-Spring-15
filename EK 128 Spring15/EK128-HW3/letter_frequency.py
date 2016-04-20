def letter_frequency(s):
    import collections
    L=s.lower()
    L=list(s)
    alphabet={}
    for i in list("abcdefghijklmnopqrstuvwxyz"):
        alphabet[i] = 0
    for i in L:
        if i in alphabet:
            alphabet[i] += 1
    out = collections.OrderedDict(sorted(alphabet.items()))
    return(out)

#Dictionaries in Python are fundamentally unordered.
#Import collections to order the dictionary alphabetically.
