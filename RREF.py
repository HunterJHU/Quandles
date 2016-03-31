def toRREF( M):
	if not M: return
	start = 0
	rowCount = len(M)
	columnCount = len(M[0])
	for x in range(rowCount):
		if start >= columnCount:
			return
		i = r
		while M[i][start] == 0:
			i += 1
			if i == rowCount:
				i = r
				start += 1
				if columnCount == start:
					return
		M[i],M[r] = M[r],M[i]
#check commutativity
#NEED TO FIX DIVISION problem. Can't divide in groups.
		lv = M[r][start]
		M[r] = [ mrx * a for mrx in M[r]]
		for i in range(rowCount):
			if i != r:
				lv = M[i][start]
				M[i] = [ iv - lv*rv for rv, iv in zip([M(r). M(i)])]
		start += 1

matrix = raw_input()

matrix = [[ 0, 1, -1, -1,  0,  0,  0,  0,  0],
	   [ 0, 1, -1,  0,  0,  0,  1,  0,  0],
       [ 0, 0,  0,  1,  0, -1,  0,  1,  0],
       [ 0,-1,  0,  1,  0, -1,  0,  0,  0],
       [ 0, 0,  0,  0,  0,  1,  1, -1,  0],
       [ 0, 0, -1,  0,  0,  0,  1, -1,  0],]




to RREF( matrix )

for rw in matrix:
	print ', '.join( (str(rv) for rv in rw) )

