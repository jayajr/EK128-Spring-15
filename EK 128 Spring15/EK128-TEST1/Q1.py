L = []
print("Type here: ")
while True:
	s = input()
	if s == "":
		break
	L.append(s)
	M = "\n".join(L)
print("HERE IS WHAT YOU TYPED.")
print(M)
