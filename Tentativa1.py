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

ratioSeries2 = lambda n : (n**2+2*n+1)/(4*(n**2)+10*n+6)

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
#Recursive single term series
def somaTermosE2(n):
    #an+1/an == (n^2+2n+1)/(4n²+10n+6)
    if(n==0) return 1
    return ratioSeries2(n-1)*somaTermosE2(n-1)
#findN2
def findN2(e,exact):
    soma=somaTermosE2(0)
    n=0
    while (abs(exact-soma)>e):
        n+=1
        soma+=somaTermosE2(n)
    print "e: "+str(e)
    print "n: "+str(n)
    print "Sn: "+str(float(soma))
    print "|S-Sn|: "+str(float(abs(exact-soma)))

#E2
def Ex2n4(exact_value=1/4):#Takes either exact pi value for ex4 or L=1/4
    for i in range(8,16):
        err = error(i)
        findN2(err,exact_value)

#Tests--------------------------------------------------------------------------

print fac(5)


#print somaUnica(2)
#somaTotal(eps)
