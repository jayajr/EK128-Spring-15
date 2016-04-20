def is_inside(px, p1, p2, p3):

	c1 = (px[0] - p1[0]) * (p2[1] - p1[1]) - (px[1] - p1[1]) * (p2[0] - p1[0])
	c2 = (px[0] - p2[0]) * (p3[1] - p2[1]) - (px[1] - p2[1]) * (p3[0] - p2[0])
	c3 = (px[0] - p3[0]) * (p1[1] - p3[1]) - (px[1] - p3[1]) * (p1[0] - p3[0])

	if c1 > 0:
		if c2 >= 0:
			if c3 >= 0:
				out = True
			if c3 < 0:
				out = False
		if c2 < 0:
			out = False
	if c1 < 0:
		if c2 <= 0:
			if c3 <= 0:
				out = True
			if c3 > 0:
				out = False
		if c2 > 0:
			out = False
	if c1 == 0:
		if c2 > 0:
			if c3 >= 0:
				out = True
			if c3 < 0:
				out = False
		if c2 < 0:
			if c3 <= 0:
				out = True
			if c3 > 0:
				out = False
		if c2 == 0:
			out = True

	return out
