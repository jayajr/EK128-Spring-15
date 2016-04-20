def area(p1,p2,p3):
	cross = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
	
	A = abs(cross) / 2

	return A

