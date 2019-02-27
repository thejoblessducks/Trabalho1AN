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


'''-----------------------------------------------------------------------------
                        Calculate machine epsilon
-----------------------------------------------------------------------------'''
#Using numpy's version
eps = np.finfo(float).eps
#Using mathmatical defenition
def macEps(func=np.float32):
    m_eps = func(1)
    while func(1)+func(m_eps) != func(1):
        m_eps_last = m_eps
        m_eps = func(m_eps) / func(2)
    return m_eps_last
#Using CC theory
eps2=2**(-(24-1))#eps=b^-(p-1) where p is the precison(24 bits) and b the base(2)

'''-----------------------------------------------------------------------------
                                Exercise 2
-----------------------------------------------------------------------------'''
#Recursive single term series
def somaUnica(k):
    af=(mt.pow(fac(k),2))/float(fac(2*k+1))
    return af
#Sn
def somaTotal(e):
    bf=9/float((2*mt.sqrt(3)))
    exato=(18)/float(mt.sqrt(3)) #por calculo de limite
    soma=0
    n=0
    while 1:
        soma=bf*somaUnica(n)
        err=exato-soma
        if(abs(err)<e):
            print n
            print abs(exato-soma)

        n+=1
    return

#Tests--------------------------------------------------------------------------
#print (1.0 + eps/10 != 1.0)
print eps #2.220446049250313*e^-16
print np.spacing(1.0) #equal to previous, 2nd numpy defenition of machine eps
print macEps() #1.1920929*e^-7
print eps2 #1.19209289551
print fac(5)


#print somaUnica(2)
#somaTotal(eps)
