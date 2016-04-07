########################################################
# Semiquandle python code by Hunter Jackson
#
# Permission granted to modify, redistribute, etc.
# Send bug reports to bjackson4@mail.usf.edu
########################################################


from sympy import *

def perminv(v):
    """inverse of a permutation"""
    out = []
    for i in range(1,len(v)+1):
       out.append(0)
    for i in range(1,len(v)+1):
       out[v[i-1]-1] = i
    return out


def pavail(v):
    """List available entries"""
    L = []
    for i in range(1,len(v)+1):
        if not i in v: L.append(i)
    return tuple(L)


def getcolumn(M,j):   # get column n from matrix M
    """Gets column n from matrix M"""
    c =[]
    for i in range(1,len(M)+1):
        c = c + [M[i-1][j-1]]
    return c


def tm(M):
    """tuple matrix"""
    out  = []
    for x in M: out.append(tuple(x))
    return tuple(out)


def lm(M):
    """list matrix"""
    out = []
    for x in M: out.append(list(x))
    return list(out)


def reptest(p):   # test whether p has repeated non-zero entries
    """Test whether p has repeated non-zero entries"""
    q = True
    L = []
    for i in range(1,len(p)+1):
        if p[i-1] != 0:
            if p[i-1] in L:
                q = False
            else:
                L.append(p[i-1])
    return q


def bfindzero(M):
    """Find position of first zero entry in a birack matrix"""
    for i in range(1,len(M[0])+1):
        for j in range(1,len(M[0])+1):
            if M[0][i-1][j-1] == 0:
                return (0,i,j)
            if M[1][i-1][j-1] == 0:
                 return (1,i,j)
    return False


def sqfill(A):
    """fill with semiquandle axioms"""
    U = lm(A[0])
    L = lm(A[1])
    n = len(U)
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for i in range(1,n+1):
            for j in range(1,n+1):
                if U[i-1][j-1] == j:
                    if L[j-1][i-1] == 0: 
                        L[j-1][i-1] = i
                        keepgoing = True
                    if L[j-1][i-1] != i: return False
                if L[i-1][j-1] == j:
                    if U[j-1][i-1] == 0: 
                        U[j-1][i-1] = i
                        keepgoing = True
                    if U[j-1][i-1] != i: return False
                if U[i-1][j-1] !=0 and L[j-1][i-1] != 0:
                    if L[U[i-1][j-1]-1][L[j-1][i-1]-1] == 0:
                        L[U[i-1][j-1]-1][L[j-1][i-1]-1] = i
                        keepgoing = True
                    if L[U[i-1][j-1]-1][L[j-1][i-1]-1] != i: 
                        return False
                    if U[L[j-1][i-1]-1][U[i-1][j-1]-1] == 0:
                        U[L[j-1][i-1]-1][U[i-1][j-1]-1] = j
                        keepgoing = True
                    if U[L[j-1][i-1]-1][U[i-1][j-1]-1] != j: 
                        return False
                for k in range(1,n+1):
                    if U[i-1][j-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] !=0 and U[j-1][k-1] != 0:
                        if U[U[i-1][j-1]-1][k-1] != 0 and U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] == 0:
                            U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] = U[U[i-1][j-1]-1][k-1]
                            keepgoing = True
                        if U[U[i-1][j-1]-1][k-1] == 0 and U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] != 0:
                            U[U[i-1][j-1]-1][k-1] = U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1] 
                            keepgoing = True
                        if U[U[i-1][j-1]-1][k-1] != U[U[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1]:
                            return False
                    if L[j-1][i-1] != 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] !=0 and U[j-1][k-1] != 0 and L[k-1][j-1] != 0 and U[i-1][L[k-1][j-1]-1] != 0:
                        if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] != 0 and L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] == 0:
                            L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] = U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1]
                            keepgoing = True
                        if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] == 0 and L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1] != 0:
                            U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] = L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]
                            keepgoing = True
                        if U[L[j-1][i-1]-1][L[k-1][U[i-1][j-1]-1]-1] != L[U[j-1][k-1]-1][U[i-1][L[k-1][j-1]-1]-1]:
                            return False
                    if L[k-1][j-1] != 0 and L[j-1][i-1]!= 0 and U[i-1][j-1] != 0 and L[k-1][U[i-1][j-1]-1] != 0:
                        if L[L[k-1][j-1]-1][i-1] != 0 and L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] == 0:
                            L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] = L[L[k-1][j-1]-1][i-1]
                            keepgoing = True
                        if L[L[k-1][j-1]-1][i-1] == 0 and L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1] != 0:
                            L[L[k-1][j-1]-1][i-1] = L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]
                            keepgoing = True
                        if L[L[k-1][j-1]-1][i-1] != L[L[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]:
                            return False
    for i in range(0,n):
        if not reptest(getcolumn(L,i+1)): 
            return False
        if not reptest(getcolumn(U,i+1)): 
            return False
    return ( tm(U),tm(L) ) 


     
def findzero(M):
    """Find position of first zero entry in a matrix"""
    out = False
    for i in range(1,len(M)+1):
        if not out:
            for j in range(1,len(M)+1):
                if M[i-1][j-1] == 0:
                    out = (i,j)
                    break
    return out


def semiquandlelist(N):
    """find all semiquandles matching pattern"""
    L = []
    L.append( ( tm(N[0]),tm(N[1]) ) )
    out = []
    while len(L)>0:
       M = (tm(L[0][0]),tm(L[0][1]))
       L[0:1] = []
       q = bfindzero(M)
       if q:
           for i in pavail(getcolumn(M[q[0]],q[2])):
               M2 = [lm(M[0]),lm(M[1])]
               M2[q[0]][q[1]-1][q[2]-1] = i
               M3 = sqfill(M2)
               if M3: L.append( ( tm(M3[0]),tm(M3[1]) ) )
       else:
           out.append( ( tm(M[0]), tm(M[1]) ) )
    for x in out:
        if not sqtest(x): out.remove(x)
    return out


def sqtest(m):
    """test for semiquandle axioms"""
    out = True
    U,L,n = m[0],m[1],len(m[0])
    for a in range(1,n+1):
        ctx,cty  = 0,0
        for x in range(1,n+1):
            if m[1][a-1][x-1] == x and m[0][x-1][a-1] == a:
                ctx = ctx +1
            if m[0][x-1][a-1] == a and m[1][a-1][x-1] == x:
                cty = cty +1
        if not(ctx == 1 and cty == 1):
            return False
        for b in range(1,n+1):
            if L[U[a-1][b-1]-1][L[b-1][a-1]-1] != a: return False
            if U[L[b-1][a-1]-1][U[a-1][b-1]-1] != b: return False
            for c in range(1,n+1):
               if U[U[a-1][b-1]-1][c-1] != U[U[a-1][L[c-1][b-1]-1]-1][U[b-1][c-1]-1]: return False
               if U[L[b-1][a-1]-1][L[c-1][U[a-1][b-1]-1]-1]!= L[U[b-1][c-1]-1][U[a-1][L[c-1][b-1]-1]-1]: return False
               if L[L[c-1][U[a-1][b-1]-1]-1][L[b-1][a-1]-1]!= L[L[c-1][b-1]-1][a-1]: return False
 
    return out


 
def sqhomfill(M,N,v):
    """fill semiquandle homomorphism v:M-->N"""
    c = True
    w = list(v)
    while c:
        c = False
        for i in range(1,len(w)+1):
            for j in range(1,len(w)+1):
                if (w[i-1] != 0 and w[j-1] != 0):
                    if w[M[0][i-1][j-1]-1] != N[0][w[i-1]-1][w[j-1]-1]:
                        if w[M[0][i-1][j-1]-1] == 0:
                            w[M[0][i-1][j-1]-1] = N[0][w[i-1]-1][w[j-1]-1] 
                            c = True
                        else:
                            return False
                    if w[M[1][i-1][j-1]-1] != N[1][w[i-1]-1][w[j-1]-1]:
                        if w[M[1][i-1][j-1]-1] == 0:
                            w[M[1][i-1][j-1]-1] = N[1][w[i-1]-1][w[j-1]-1] 
                            c = True
                        else:
                            return False
    return w


def hfindzero(f):   #find zero entry in homomorphism
    """find zero in homomorphism template"""
    j = -1
    for i in range(0,len(f)):
        if f[i] == 0: 
            j = i+1
            break
    if j < 0: out = False
    else: out = j
    return out


def sqhomlist(M,N):
    """find semiquandle homomorphisms f:M-->N"""
    z = []    
    for i in range(1,len(M[0])+1):
        z = z + [0]
    L = [z]
    out = []
    while len(L) != 0:
        w = L[0]
        L[0:1] = []  
        if w:
            i = hfindzero(w)
            if not i:
                out.append(w)
            else:
                for j in range(1,len(N[0])+1):
                    phi = list(w)
                    phi[i-1] = j
                    v = sqhomfill(M,N,phi)
                    if v: L.append(tuple(v))
    return out     



def sqisolist(M,N):
    """find semiquandle isomorphisms f:M-->N"""
    z = []    
    for i in range(1,len(M[0])+1):
        z = z + [0]
    L = [z]
    out = []
    while len(L) != 0:
        w = L[0]
        L[0:1] = []  
        if w:
            i = hfindzero(w)
            if not i: 
                if reptest(w): 
                    out.append(tuple(w))
            else:
                for j in range(1,len(N[0])+1):
                    if not j in w:
                        phi = list(w)
                        phi[i-1] = j
                        v = sqhomfill(M,N,phi)
                        if v: L.append(tuple(v))
    return out     


def sqautlist(M):
    return sqisolist(M,M)
    
    

def sqpdhomlist(PD,W):   # list semiquandle homomorphisms
    """Lists homomorphisms from fundamental semiquandle of planar diagram"""
    z = []
    U,L = W[0], W[1]
    for i in range(1,2*len(PD)+1):
        z = z + [0]
    L1 = [z]
    out = []
    while len(L1) != 0:
        w = L1[0]
        L1[0:1] = []  
        if w:
            i = hfindzero(w)
            if not i:
                out.append(w)
            else:
                for j in range(1,len(U)+1):
                    phi = list(w)
                    phi[i-1] = j
                    v = sqpdhomfill(PD,U,L,phi)
                    if v: L1.append(tuple(v))
    return out     


def sqpdhomfill(PD,U,L,phi):   # fill in homomorphism
    """Fills in entries in a homomorphism"""
    f = phi
    c = True
    while c:
        c = False
        for X in PD:
            if X[0] == 0.5:
                if f[X[1]-1] != 0 and f[X[4]-1] != 0:
                    if f[X[3]-1] == 0: 
                        f[X[3]-1] = U[f[X[1]-1]-1][f[X[4]-1]-1]
                        c = True
                    elif f[X[3]-1] != U[f[X[1]-1]-1][f[X[4]-1]-1]:
                        return False
                    if f[X[2]-1] == 0: 
                        f[X[2]-1] = L[f[X[4]-1]-1][f[X[1]-1]-1]
                        c = True
                    elif f[X[2]-1] != L[f[X[4]-1]-1][f[X[1]-1]-1]:
                        return False
    return f



def subsemi(L2,S):
    """Find subsemiquandle generated by L"""
    out = list()
    for x in L2:
       if not x in out: out.append(x)
    c = True
    while c:
       c = False
       for x in out:
          for y in out:
              if not S[0][x-1][y-1] in out:
                 out.append(S[0][x-1][y-1])
                 c = True
              if not S[1][x-1][y-1] in out:
                 out.append(S[1][x-1][y-1])
                 c = True
    return out


def sqpoly(PD,S):
    """enhanced semiquandle counting invariant"""
    z = Symbol('z')
    H = sqpdhomlist(PD,S)
    out = 0
    for h in H:
       out = out + z**(len(subsemi(h,S)))
    return out


##############################
# Singular Semiquandles
##############################


def ssqfind(M):
    """find singular structures compatible with semiquandle M"""
    n=len(M[0])
    z = []
    zz = []
    for i in range(0,n): z.append(0)
    for i in range(0,n): zz.append(tuple(z))
    L=[(zz,zz)]
    out = []
    while len(L)>0:
       w = L[0]
       L[0:1] = []  
       q = bfindzero(w)
       if q:
          for i in range(1,n+1):
             M2 = [lm(w[0]),lm(w[1])]
             M2[q[0]][q[1]-1][q[2]-1] = i
             M3 = ssqfill(M,M2)
             if M3: L.append( ( tm(M3[0]),tm(M3[1]) ) )
       else:
          out.append( ( tm(w[0]), tm(w[1]) ) )
    return out

    
def ssqpdhomfill(PD,N,S,phi):   # fill in homomorphism
    """Fills in entries in a homomorphism"""
    f = phi
    c = True
    while c == True:
        c = False
        for X in PD:
            if X[0] == 0.5:
                if f[X[1]-1] != 0 and f[X[4]-1] != 0:
                    if f[X[3]-1] == 0: 
                        f[X[3]-1] = N[0][f[X[1]-1]-1][f[X[4]-1]-1]
                        c = True
                    elif f[X[3]-1] != N[0][f[X[1]-1]-1][f[X[4]-1]-1]:
                        return False
                    if f[X[2]-1] == 0: 
                        f[X[2]-1] = N[1][f[X[4]-1]-1][f[X[1]-1]-1]
                        c = True
                    elif f[X[2]-1] != N[1][f[X[4]-1]-1][f[X[1]-1]-1]:
                        return False
            if X[0] == 2:
                if f[X[1]-1] != 0 and f[X[4]-1] != 0:
                    if f[X[3]-1] == 0: 
                        f[X[3]-1] = S[0][f[X[1]-1]-1][f[X[4]-1]-1]
                        c = True
                    elif f[X[3]-1] != S[0][f[X[1]-1]-1][f[X[4]-1]-1]:
                        return False
                    if f[X[2]-1] == 0: 
                        f[X[2]-1] = S[1][f[X[4]-1]-1][f[X[1]-1]-1]
                        c = True
                    elif f[X[2]-1] != S[1][f[X[4]-1]-1][f[X[1]-1]-1]:
                        return False
    return f



def ssqfill(M,A):
    Uh = lm(A[0])
    Lh = lm(A[1])
    U,L = M[0],M[1]
    n = len(U)
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (Lh[j-1][i-1]!= 0 and Uh[i-1][j-1] !=0):
                    if Uh[L[j-1][i-1]-1][U[i-1][j-1]-1] == 0:
                        Uh[L[j-1][i-1]-1][U[i-1][j-1]-1] = U[Lh[j-1][i-1]-1][Uh[i-1][j-1]-1]
                        keepgoing = True
                    if Uh[L[j-1][i-1]-1][U[i-1][j-1]-1] != U[Lh[j-1][i-1]-1][Uh[i-1][j-1]-1]:
                        return False
                    if Lh[U[i-1][j-1]-1][L[j-1][i-1]-1] == 0:
                        Lh[U[i-1][j-1]-1][L[j-1][i-1]-1] = L[Uh[i-1][j-1]-1][Lh[j-1][i-1]-1]
                        keepgoing = True
                    if Lh[U[i-1][j-1]-1][L[j-1][i-1]-1] != L[Uh[i-1][j-1]-1][Lh[j-1][i-1]-1]:
                        return False
                for k in range(1,n+1):
                    if Uh[i-1][L[k-1][j-1]-1] != 0:
                        if Uh[U[i-1][j-1]-1][k-1] == 0: 
                            Uh[U[i-1][j-1]-1][k-1] = U[Uh[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1]
                            keepgoing = True
                        if Uh[U[i-1][j-1]-1][k-1] != U[Uh[i-1][L[k-1][j-1]-1]-1][U[j-1][k-1]-1]:
                            return False
                        if Lh[k-1][U[i-1][j-1]-1] !=0:
                            if U[L[j-1][i-1]-1][Lh[k-1][U[i-1][j-1]-1]-1] != L[U[j-1][k-1]-1][Uh[i-1][L[k-1][j-1]-1]-1]:
                                return False
                    if Lh[k-1][U[i-1][j-1]-1] != 0:
                        if Lh[L[k-1][j-1]-1][i-1] == 0:
                            Lh[L[k-1][j-1]-1][i-1] = L[Lh[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]
                            keepgoing = True
                        if Lh[L[k-1][j-1]-1][i-1] != L[Lh[k-1][U[i-1][j-1]-1]-1][L[j-1][i-1]-1]:
                            return False
    return( ( tm(Uh),tm(Lh) ) )


def ssqpdhomlist(PD,N,S):   # list semiquandle homomorphisms
    """Lists homomorphisms from fundamental semiquandle of planar diagram"""
    z = []
    for i in range(1,2*len(PD)+1):
        z = z + [0]
    L1 = [z]
    out = []
    while len(L1) != 0:
        w = L1[0]
        L1[0:1] = []  
        if w:
            i = hfindzero(w)
            if not i:
                out.append(w)
            else:
                for j in range(1,len(N[0])+1):
                    phi = list(w)
                    phi[i-1] = j
                    v = ssqpdhomfill(PD,N,S,phi)
                    if v: L1.append(tuple(v))
    return out     



def ssqpoly(PD,S,SS):
    """enhanced semiquandle counting invariant"""
    z = Symbol('z')
    H = ssqpdhomlist(PD,S,SS)
    out = 0
    for h in H:
       out = out + z**(len(subsing(h,S,SS)))
    return out



def subsing(L2,S,SS):
    """Find subsemiquandle generated by L"""
    out = []
    for x in L2:
       if not x in out: out.append(x)
    c = True
    while c:
       c = False
       for x in out:
          for y in out:
              if not S[0][x-1][y-1] in out:
                 out.append(S[0][x-1][y-1])
                 c = True
              if not S[1][x-1][y-1] in out:
                 out.append(S[1][x-1][y-1])
                 c = True
              if not SS[0][x-1][y-1] in out:
                 out.append(SS[0][x-1][y-1])
                 c = True
              if not SS[1][x-1][y-1] in out:
                 out.append(SS[1][x-1][y-1])
                 c = True
    return out


####################################
# Virtual singular semiquandles
####################################


def ssqautlist(M,N):
    T = sqautlist(M)
    out = []
    for x in T:
        inc = True
        for i in range(1,len(M[0])+1):
            for j in range(1,len(M[0])+1):
                 if (N[0][x[i-1]-1][x[j-1]-1] != x[N[0][i-1][j-1]-1]) or (N[1][x[i-1]-1][x[j-1]-1] != x[N[1][i-1][j-1]-1]):
                     inc = False
        if inc: out.append(x)
    return out



def vssqpdhomfill(PD,N,S,v,phi):   # fill in homomorphism
    """Fills in entries in a homomorphism"""
    f = phi
    c = True
    vinv = perminv(v)
    while c == True:
        c = False
        for X in PD:
            if X[0] == 0.5:
                if f[X[1]-1] != 0 and f[X[4]-1] != 0:
                    if f[X[3]-1] == 0: 
                        f[X[3]-1] = N[0][f[X[1]-1]-1][f[X[4]-1]-1]
                        c = True
                    elif f[X[3]-1] != N[0][f[X[1]-1]-1][f[X[4]-1]-1]:
                        return False
                    if f[X[2]-1] == 0: 
                        f[X[2]-1] = N[1][f[X[4]-1]-1][f[X[1]-1]-1]
                        c = True
                    elif f[X[2]-1] != N[1][f[X[4]-1]-1][f[X[1]-1]-1]:
                        return False
            if X[0] == 2:
                if f[X[1]-1] != 0 and f[X[4]-1] != 0:
                    if f[X[3]-1] == 0: 
                        f[X[3]-1] = S[0][f[X[1]-1]-1][f[X[4]-1]-1]
                        c = True
                    elif f[X[3]-1] != S[0][f[X[1]-1]-1][f[X[4]-1]-1]:
                        return False
                    if f[X[2]-1] == 0: 
                        f[X[2]-1] = S[1][f[X[4]-1]-1][f[X[1]-1]-1]
                        c = True
                    elif f[X[2]-1] != S[1][f[X[4]-1]-1][f[X[1]-1]-1]:
                        return False
            if X[0] == 0:
                if f[X[1]-1] !=0 and f[X[3]-1] == 0:
                    f[X[3]-1] = v[f[X[1]-1]-1]
                    c = True
                if f[X[3]-1] !=0 and f[X[1]-1] == 0:
                    f[X[1]-1] = vinv[f[X[3]-1]-1]
                    c = True
                if f[X[3]-1] != f[X[1]-1]:
                    return False
                if f[X[4]-1] !=0 and f[X[2]-1] == 0:
                    f[X[2]-1] = vinv[f[X[4]-1]-1]
                    c = True
                if f[X[2]-1] !=0 and f[X[4]-1] == 0:
                    f[X[4]-1] = v[f[X[2]-1]-1]
                    c = True
                if f[X[4]-1] != f[X[2]-1]:
                    return False
    return f

def vssqpdhomlist(PD,N,S,v):   # list semiquandle homomorphisms
    """Lists homomorphisms from fundamental semiquandle of planar diagram"""
    z = []
    for i in range(1,2*len(PD)+1):
        z = z + [0]
    L1 = [z]
    out = []
    while len(L1) != 0:
        w = L1[0]
        L1[0:1] = []  
        if w:
            i = hfindzero(w)
            if not i:
                out.append(w)
            else:
                for j in range(1,len(N[0])+1):
                    phi = list(w)
                    phi[i-1] = j
                    w2 = vssqpdhomfill(PD,N,S,v,phi)
                    if w2: L1.append(tuple(w2))
    return out     


def vssqpoly(PD,S,SS,v):
    """enhanced semiquandle counting invariant"""
    z = Symbol('z')
    H = vssqpdhomlist(PD,S,SS,v)
    out = 0
    for h in H:
       out = out + z**(len(vsubsing(h,S,SS,v)))
    return out




def vsubsing(L2,S,SS,v):
    """Find virtual subsemiquandle generated by L"""
    out = []
    vinv = perminv(v)
    for x in L2:
       if not x in out: out.append(x)
    c = True
    while c:
       c = False
       for x in out:
          if not v[x-1] in out:
              out.append(v[x-1])
              c = True
          if not vinv[x-1] in out:
              out.append(vinv[x-1])
              c = True
          for y in out:
              if not S[0][x-1][y-1] in out:
                 out.append(S[0][x-1][y-1])
                 c = True
              if not S[1][x-1][y-1] in out:
                 out.append(S[1][x-1][y-1])
                 c = True
              if not SS[0][x-1][y-1] in out:
                 out.append(SS[0][x-1][y-1])
                 c = True
              if not SS[1][x-1][y-1] in out:
                 out.append(SS[1][x-1][y-1])
                 c = True
    return out

