##############################################################################
#
# Version 14
# Loops over coefficient groups
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
	shape = (len(M), len(M[0]))
	pairs = int(sqrt(shape[1])) + 1
	for i in range(shape[0]):
		for j in range(0, shape[1], pairs):
			M[i][j] = 0
			M[i][j] = 0
			M[i][j] = 0


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


def main(M):
	length = len(M)
	cohomology_group = []
	generator_list = []
	

	relations = listRelations(M)
	zeroDoubles(relations)
	stored_relations = relations

### Insert prime loop here
	relations = stored_relations
	group = GF(4, 'a')

	relation_size = (len(relations), len(relations[0]))
	MS = MatrixSpace(group, relation_size[0], relation_size[1])
	relations = MS(relations)
	relations = array(relations.echelon_form())
	relations = removeTrivial(relations)

	######
	# Substitute into general 2-cocycle f 
	variable_num = len(relations[0])

	function = identity(variable_num, dtype=int)
	zeroDoubles(function)

	relation_size = (len(relations), len(relations[0]))
	for i in range(relation_size[0]):
		for j in range(relation_size[1]):
			if relations[i][j] != 0:
				function[j] += -relations[i]
				break

	function = function.T

	function = removeTrivial(function)

	function_size = (len(function), len(function[0]))
	MS = MatrixSpace(group, function_size[0], function_size[1])
	function = MS(list(function))
	function = list(function.echelon_form())

	######
	# Computes coboundary matrix
	cobs = matrixCoboundaries(M)

	MS = MatrixSpace(group, len(cobs), len(cobs[0]))
	cobs = MS(cobs)
	cobs = cobs.echelon_form()
	cobs = list(removeTrivial(array(cobs)))

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

	function = removeTrivial(array(function))
	MS = MatrixSpace(group, function.shape[0], function.shape[1])
	function = MS(list(function))
	function = function.echelon_form()

	function_length = len(list(function))
	for Z in range(function_length):
		cohomology_group.append('4')

	for generator in function:
		generator = list(generator)
		generator_list.append(generator)

	return (cohomology_group, generator_list)

if __name__ == "__main__":
	counter = 1

	for M in quandle_list:
		# new_quandle_size = len(M)
		# if new_quandle_size > quandle_size:
		# 	counter = 1
		quandle_size = len(M)
		
		if quandle_size == 12:
			answer = main(M)
			print "{}_{}:".format(quandle_size, counter), answer[0]
			print "generators: ", answer[1]
			# print
			counter += 1




