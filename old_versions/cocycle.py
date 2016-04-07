#################################
#2 cocycle computations
#Hunter Jackson
#################################

from numpy import *
from sympy import *
from quandlelist import *
from math import sqrt


def getcolumn(M,j):   
    c =[]
    for i in range(1,len(M)+1):
        c.append(M[i-1][j-1])
    return c
    

def list(M):
    out = []
    for x in M: out.append(list(x))
    return list(out)
    
def transpose(M):
    out=[]
    for i in range(1,len(M[0])+1):
        r = []
        for j in range(1,len(M)+1):
            r.append(M[j-1][i-1])
        out.append(r)
    return out


def reptest(p):   
    q = True
    L = []
    for i in range(1,len(p)+1):
        if p[i-1] != 0:
            if p[i-1] in L:
                q = False
            else:
                L.append(p[i-1])
    return q

def selfdistributivity(N):
    c = True
    con = False
    M = lm(N)
    while c:
        c = False
        for i in range(1,len(M)+1):
            for j in range(1,len(M)+1):
                for k in range(1,len(M)+1):
                    if M[i-1][j-1] != 0 and M[M[i-1][j-1]-1][k-1] != 0:
                        if M[i-1][k-1] != 0 and M[j-1][k-1] != 0:
                            if M[M[i-1][j-1]-1][k-1] != M[M[i-1][k-1]-1][M[j-1][k-1]-1]:
                                if M[M[i-1][j-1]-1][k-1] == 0:
                                    M[M[i-1][j-1]-1][k-1] = M[M[i-1][k-1]-1][M[j-1][k-1]-1]
                                    c = True
                                elif M[M[i-1][k-1]-1][M[j-1][k-1]-1] == 0:
                                    M[M[i-1][k-1]-1][M[j-1][k-1]-1] = M[M[i-1][j-1]-1][k-1]
                                    c = True
                                else:
                                    con = True
    if con: M = False
    return M
    
def cocycletest(R,v,n):

    N=rackrank(R)
    m=len(R)
#    r=[]
    out = True
    for x in range(1,len(R)+1):
        for y in range(1,len(R)+1):
            for z in range(1,len(R)+1): 
                if n ==0:
                    if (v[m*(x-1)+y-1]+v[m*(R[x-1][y-1]-1)+z-1] -v[m*(x-1)+z-1]-v[m*(R[x-1][z-1]-1)+R[y-1][z-1]-1]) != 0:
                        return False
                if n!=0:
                    if (v[m*(x-1)+y-1]+v[m*(R[x-1][y-1]-1)+z-1] -v[m*(x-1)+z-1]-v[m*(R[x-1][z-1]-1)+R[y-1][z-1]-1]) %n != 0:
                        return False
        t,x2=0,x
        for k in range(0,N):
            if n == 0:
                t=t+v[m*(x2-1)+x2-1]
            if n !=0:
                t=(t+v[m*(x2-1)+x2-1])%n
            x2=R[x2-1][x2-1]
        if t != 0:
            return False
    return True


    for i in range(0,len(R)**2):
        r.append(0)
    for x in range(1,len(R)+1):
       r2 = list(tuple(r))
       y = x
       for i in range(0,N):
           y = R[y-1][y-1]
       r2[len(R)*(y-1)+y-1] = r2[len(R)*(y-1)+y-1] +1
    if mm([v],mtranspose([r2]),n)[0][0]%n != 0:
         out = False
    return out

     

def available(v):
    L = []
    for i in range(1,len(v)+1):
        if not i in v: L.append(i)
    return tuple(L)


	


