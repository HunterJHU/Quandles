##############################################################################
#
# Version 13
# Rewriting row reduction using sage 
#
##############################################################################

from numpy import *
import sympy as sp
from math import sqrt
from quandlelist import *
from sage.all import *
from operator import sub
 
# Prints numpy array completely
# set_printoptions(threshold=nan)



def computeCoeff(triple, matrix):
	### Equation obtained from evaluating element of Z^2 in 2-cocycle equation
	n = len(matrix)
	current_eq = []
	p, q, r = triple[0], triple[1], triple[2]
	a, b, c, d  = (p, r), (matrix[p, r], matrix[q, r]), (p, q), (matrix[p, q], r)
	constants = [a,b,c,d]
	for x in range(n):
		for y in range(n):
				if (x,y) in constants:
					if ((x,y) == a or (x,y) == b) and ((x,y) == c or (x,y) == d):
						current_eq.append(0)
					elif ((x,y) == a or (x,y) == b):
						current_eq.append(1)
					elif ((x,y) == c or (x,y) == d):
						current_eq.append(-1)
				else:
					current_eq.append(0)
	return current_eq

def listRelations(M):
	### Lists n^3 equations obtained by evaluating triples in 2-cocycle equation
	n = len(M)
	list_of_equations = []
	for x in range(n):
		for y in range(n):
			for z in range(n):
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
	for i in range(length):
		for j in range(length):
			cob = chi(i,n) - chi(M[i,j], n)
			coboundary_row.append(cob)
	return coboundary_row


def matrixCoboundaries(M):
	### Lists coboundary computations in a matrix
	length = len(M)
	coboundary_matrix = []
	for i in range(length):
		coboundary_matrix.append(computeCoboundary(M,i))
	return coboundary_matrix


def chi(m,n):
	### Characteristic functions mapping the quandle to an abelian group
	if m == n:
		return 1
	else:
		return 0


def zeroDoubles(M):
	# Sets all entries in columns corresponding to an ordered pair of the form (x, x) to the zero
	shape = M.shape
	pairs = int(sqrt(shape[1])) + 1
	for i in range(shape[0]):
		for j in range(0, shape[1], pairs):
			M[i, j] = 0
			M[i, j] = 0
			M[i, j] = 0


def removeTrivial(array):
	idxs = any(array != 0, axis=1)
	return array[idxs, :]


def removeDuplicates(array):
# Removes duplicate rows
	i = 0
	while i < len(array):
		store = -array[i]
		for row in array[i+1:]:
			if (store==row).all():
				array = delete(array, i, axis=0)
				i -= 1
		i += 1
	return array


#########
#########
M = C3_1	# Computations based on choice for M
mod_num = 2 # Determined the group coefficents are in. 0 implies Z

###
relations = array(listRelations(M))
print "The relations obtained by plugging in triples:"
zeroDoubles(relations)
print relations
print


######
# Row reduce over a group.
group = ZZ
if mod_num != None: 
	group = GF(mod_num)

MS = MatrixSpace(group, relations.shape[0], relations.shape[1])
relations = MS(list(relations))
relations = array(relations.echelon_form())
relations = removeTrivial(relations)
print relations
print

######
# Substitute into general 2-cocycle f 
variable_num = relations.shape[1]

function = identity(variable_num, dtype=int)
zeroDoubles(function)
print function
print

size = relations.shape
for i in range(size[0]):
	for j in range(size[1]):
		if relations[i][j] != 0:
			function[j] += -relations[i]
			break
print function
print

function = function.T
print "Transpose"
print function
print


print "remove trivial"
function = removeTrivial(function)
print function
print


print "row reduce"
MS = MatrixSpace(group, function.shape[0], function.shape[1])
function = MS(list(function))
function = list(function.echelon_form())
print array(function)
print


######
# Computes coboundary matrix
cobs = matrixCoboundaries(M)
print "Coboundary matrix:"
print array(cobs)
print


MS = MatrixSpace(group, len(cobs), len(cobs[0]))
cobs = MS(cobs)
cobs = cobs.echelon_form()
cobs = list(removeTrivial(array(cobs)))
print "Coboundaries reduced over a group:"
print array(cobs)
print

for row in cobs:
	row = list(row)
	index_of_cob = None
	for entry in row:
		if entry != 0:
			index_of_cob = list(row).index(entry)
			break
	for func_row in function:
		index_of_function = None
		for func_entry in func_row:
			if func_entry != 0:
				index_of_function = list(func_row).index(func_entry)
				break
		if index_of_cob == index_of_function:
			function[function.index(func_row)] = map(sub, function[function.index(func_row)], func_row)
			break

print array(function)
print 

function = removeTrivial(array(function))
MS = MatrixSpace(group, function.shape[0], function.shape[1])
function = MS(list(function))
function = function.echelon_form()
print "We have"
print function
print







