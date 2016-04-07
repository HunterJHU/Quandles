##############################################################################
#
# Version 12
# Rewriting row reduction using sage 
# Note that no safe build system is created in sublime (yet)
#
##############################################################################

from numpy import *
import sympy as sp
from math import sqrt
from quandlelist import *
from sage import *



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
	### Sets all entries in columns corresponding to an ordered pair of the form (x, x) to the zero
	shape = M.shape
	pairs = int(sqrt(M.shape[1])) + 1
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
M = C4_1	# Computations based on choice for M
mod_num = 3 # Determined the group coefficents are in. 0 implies Z

###
relations = array(listRelations(M))
print "The relations obtained by plugging in triples:"
zeroDoubles(relations)
print relations
print


# ###
# # Only necessary when quandle is not connected
# relations = array(removeTrivial(relations))
# print "(If not connected quandle) Removed trivial rows:"
# print relations
# print


# relations = removeDuplicates(relations)
# print "We removed duplicate rows"
# print relations
# print


######
# Row reduce over a group.
group = ZZ
if mod_num != None: group = GF(mod_num)

MS = MatrixSpace(group, relations.shape[0], relations.shape[1])
print MS
relations = MS(list(relations))
relations = array(relations.echelon_form())
relations = removeTrivial(relations)
print relations

######
# Substitute into general 2-cocycle f 
variable_num = relations.shape[1]

variables = sp.symbols('L0:%d'% variable_num)
chis = sp.symbols('c0:%d'% variable_num)

function = 0
for i in range(variable_num):
		function += variables[i]*chis[i]


relation_equations = []
for row in relations:
	expr = 0
	for i in range(variable_num):
		expr += row[i]*variables[i]
	relation_equations.append(expr)

print relation_equations
print

solved_relations = sp.solve(relation_equations, manual=True)
print solved_relations
print

if type(solved_relations) == list:
	for r in solved_relations:
		function = function.subs(r)
else:
	function = function.subs(solved_relations)
print function
print


###### TODO: remove lambdas that are zero
torsion_variables = []	# Deleltes lambdas that are torsion
for j in range(0, variable_num, int(sqrt(variable_num)) + 1):
	torsion_variables.append(j)

for n in torsion_variables:
	function = function.subs(variables[n], 0)

print sp.Poly(function, variables)
print

coc_gens = sp.Poly(function, variables).coeffs()
for item in coc_gens:
	if mod_num != None:
		print item.expand(modulus=mod_num)
	else: print item
print

######
# Computes coboundary matrix
cobs = array(matrixCoboundaries(M))
print "Coboundary matrix:"
print cobs
print


if mod_num != None:
	cobs = cobs % mod_num
	print "Coboundaries modded by %d:" % mod_num
	print cobs
	print

MS = MatrixSpace(group, cobs.shape[0], cobs.shape[1])
print MS
cobs = MS(list(cobs))
cobs = array(cobs.echelon_form())
cobs = removeTrivial(cobs)
print "Coboundaries reduced over a group:"
print cobs
print

if mod_num != None:
	cobs = cobs % mod_num
	print "Reduced Coboundaries modded by %d:" % mod_num
	print cobs
	print


######
cob_gens =[]
for row in cobs:
	expr = 0
	for i in range(variable_num):
		expr = expr + row[i]*chis[i]
	cob_gens.append(expr)

print cob_gens
print 

solved_coboundaries = sp.solve(cob_gens, manual=True)
print solved_coboundaries
print

if type(solved_coboundaries) == list:
	for r in solved_coboundaries:
		function = function.subs(r)
else:
	function = function.subs(solved_coboundaries)

print "Substitute solved coboundaries into function:"
print sp.Poly(function, variables)
print

finallist =[]
for coefficient in sp.Poly(function, variables).coeffs():
	print (coefficient).expand(modulus=mod_num)
	finallist.append(coefficient)










