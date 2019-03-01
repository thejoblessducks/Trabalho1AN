from __future__ import division
import numpy as np
import math as mt
'''-----------------------------------------------------------------------------
                        Auxiliar Functions: factorial
-----------------------------------------------------------------------------'''
#Recursive factorial
def fac(n):
    if n==0:
        return 1;
    return n*fac(n-1)

error = lambda x : 1.0*(10**-x) #returns value of error being used

#ratioSeries2 = lambda n : (n**2+2*n+1)/(4*(n**2)+10*n+6)

'''-----------------------------------------------------------------------------
                        Calculate machine epsilon
-----------------------------------------------------------------------------'''
#Using numpy's version -- double precision
eps = np.finfo(float).eps
#Using mathmatical defenition -- single precision
def macEps(func=np.float32):
    m_eps = func(1)
    while func(1)+func(m_eps) != func(1):
        m_eps_last = m_eps
        m_eps = func(m_eps) / func(2)
    return m_eps_last
#Using CC theory  -- single precision
eps2=2**(-(24-1))#eps=b^-(p-1) where p is the precison(24 bits) and b the base(2)
def mEps():
    e=1
    while (1+e)<1:
        e/=2
    return e*2


'''-----------------------------------------------------------------------------
                                Exercise 2
-----------------------------------------------------------------------------'''
#ratioSeries2
def ratioSeries2(n):
    return ((n**2)+2*n+1)/((4*(n**2))+10*n+6)
#findN2
def findN2(e,exact):
    bf=9/(2*mt.sqrt(3))
    a=1
    sum=a
    Sn=bf*sum
    n=0
    while (abs(exact-Sn)>e):
        a=ratioSeries2(n)*a
        n+=1
        sum+=a
        Sn=bf*sum
    print "     |-n: "+str(n)
    print "     |-Sn: "+str(bf*sum)
    print "     |-|S-Sn|: "+str(abs(exact-Sn))
    return
#E2
def Ex2n4(exact_value):#Takes either exact pi value for ex4 or L=1/4
    for i in range(8,16):
        err = error(i)
        print "Erro "+str(err)+":"
        findN2(err,exact_value)
    return

#Tests--------------------------------------------------------------------------
print mt.pi
print "Exercicio 2:"
Ex2n4(mt.pi)
print eps

#print somaUnica(2)
#somaTotal(eps)
