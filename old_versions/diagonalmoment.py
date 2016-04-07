import itertools as IT
from numpy import *



def diagonalmoment(l):

    L = l[:]
    return_list = [[] for i in range(len(L))]

    for line in range(len(L)):
        L[line].reverse()
        i = line

        for elem in L[line]:
            if i >= len(return_list):
                return_list.append([])

            return_list[i].append(elem)
            i += 1

    return_list.reverse()
    return return_list#

import itertools as IT

L = [  [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9] ]
N = len(L)
d = dict()
for i,j in IT.product(range(N), repeat=2):
    d.setdefault(j-i, []).append((i,j))

print([[L[i][j] for i,j in d[k]] for k in range(-N+1, N)])    
