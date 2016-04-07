##############################################################################
### This programs checks the row reduced 
### cocycle matrix to see if there are any torsion elemenets.
###
### Version 2 uses update rowReduce function, where z does not need
### to be specified.
###
###############################################################################

from numpy import *
from sympy import *
from math import sqrt
from quandlelist import *



def computeCoeff(triple, matrix):
	### Equation obtained from evaluating element of Z^2 in 2-cocycle equation
	n = len(matrix)
	current_eq = []
	p, q, r = triple[0], triple[1], triple[2]
	a, b, c, d  = (p, r), (matrix[p, r], matrix[q, r]), (p, q), (matrix[p, q], r)
	constants = [a,b,c,d]
	for x in range(0, n):
		for y in range(0, n):
				if (x,y) in constants:
					if ((x,y) == a or (x,y) == b) and ((x,y) == c or (x,y) == d):
						current_eq.append(0)
					elif ((x,y) == a or (x,y) == b):
						current_eq.append(1)
					elif ((x,y) == c or (x,y) == d):
						current_eq.append(-1)
				else:
					current_eq.append(0)
	#print triple
	#equation = []
	#for i in range(0, len(current_eq)):
	#	if current_eq[i] != 0:
	#		equation.append("%d(%d,%d)" % (current_eq[i] , (i / 4), (i % 4)))
	#print equation
	return current_eq


def listEquations(M):
	### Lists n^3 equations obtained by evaluating triples in 2-cocycle equation
	n = len(M)
	list_of_equations = []
	for x in range(0, n):
		for y in range(0, n):
			for z in range(0, n):
				triple = (x,y,z)
				if (x == y) or (y == z):
					pass
				else:
					list_of_equations.append(computeCoeff(triple, M))
	return list_of_equations
		


def computeCoboundary(M, n):
	### Given Cayley tables, computes the delta(chi_n)
	length = len(M)
	coboundary_row = []
	for i in range(0, length):
		for j in range(0, length):
			cob = chi(i,n) - chi( M[i,j],n )
			coboundary_row.append(cob)
	return coboundary_row


def matrixCoboundaries(M):
	### Lists coboundary computations in a matrix
	length = len(M)
	coboundary_matrix = []
	for i in range(0, length):
		coboundary_matrix.append(computeCoboundary(M,i))
	return coboundary_matrix


def chi(m,n):
	### Characteristic functions mapping the quandle to an abelian group
	if m == n:
		return 1
	else:
		return 0


def zeroDoubles(M):
	### Sets all entries in columns corresponding to an ordered pair of the form (x, x) to the zero
	for i in range(0, M.shape[0]):
		for j in range(0, M.shape[1], int(sqrt(M.shape[1])) + 1):
			M[i, j] = 0
			M[i, j] = 0
			M[i, j] = 0


def display(M):
	### Use to display matrix if python shorten output
	for i in range(0, len(M)):
		print M[i]


def computeBetti(M):
	### Compute the Betti number for the cohomology group with dim Z^2 - dim B^2
	reduced_list = array(listEquations(M))
	zeroDoubles(reduced_list)
	ker_matrix = Matrix(reduced_list).rref()
	ker_matrix_free_variables = array(ker_matrix[0]).shape[1] - sqrt(array(ker_matrix[0]).shape[1]) - len(ker_matrix[1])
	im_matrix =  Matrix(matrixCoboundaries(M)).rref()
	im_matrix_pivots = len(im_matrix[1])
	print "%d" % (ker_matrix_free_variables - im_matrix_pivots)

def rowReduce(array):
	### Row reduces over a group - n is the coefficients it checks
	M = array.copy()
	rows = M.shape[0]
	cols = M.shape[1]
	done_list = []
	z = 1
	repeat = True
	while repeat == True:
		max_index = argmax(M)
		max_entry = M[max_index / cols][max_index % cols]
		min_index = argmin(M)
		min_entry = M[min_index / cols][min_index % cols]
		if z > max_entry or (abs(min_entry)) > z:
			repeat = False
		for j in range(0, cols):
			for i in range(0, rows):
				if i not in done_list:
					if M[i][j] == -z:
						store = M[i]
						for k in range(i+1, rows):
							if M[k][j] == -z:
								M[k] = M[k] - store
							if M[k][j] == z:
								M[k] = M[k] + store
						done_list.append(i)
					if M[i][j] == z:
						store = M[i]
						for k in range(i+1, rows):
							if M[k][j] == z:
								M[k] = M[k] - store
							if M[k][j] == -z:
								M[k] = M[k] + store
						done_list.append(i)
		z += 1
	return M

counter = 1
for M in quandle_list:
	print "Checking %d" % counter
	equations = array(listEquations(M))
	zeroDoubles(equations)
	

	mylist = rowReduce(equations)
	
	
	### Removes zero rows
	newlist =[]
	for i in range(0, mylist.shape[0]):
		for entry in list(mylist[i]):
			if entry != 0:
				newlist.append(list(mylist[i]))
				break
	
	
	eqlist = array(newlist)
	
	
	### Determined the group coefficents are in. 0 implies Z
	mod_num = 0
	
	if mod_num == 0:
		uselist = eqlist
	else:
		modlist = (array(newlist) % mod_num)
		print "Modded by %d:" % mod_num
		display(modlist)
		print "\n"
		uselist = modlist
	
	for row in uselist:
		n = 0
		for entry in row:
			if entry != 0:
				n += 1
		if n == 1:
			print "Please check the follow quandle %d" % counter
			break
	counter += 1
		

	 





