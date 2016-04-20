def twoSums(L):
	A=[]
	B=[]
	for a in L:
		if a > 0:
			A.append(a)
		if a < 0:
			B.append(a)
	A=sum(A)
	B=sum(B)
	return(A,B)

#L=[]
#cont=1
#while cont == 1:
#	L.append(int(input("Add a value to the list: ")))
#	m=str(input("Would you like to add more values: (Y)es or (N)o? "))
#	if (m == 'Y' or m == 'y'):
#		cont = 1
#	elif (m == 'N' or m == 'n'):
#		cont = 0
#k=twoSums(L)
#print(k)