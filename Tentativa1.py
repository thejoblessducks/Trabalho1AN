from __future__ import division
import numpy as np
import math as mt
'''-----------------------------------------------------------------------------
                        Auxiliar Functions: factorial-not used
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
                                Exercise 2/4
-----------------------------------------------------------------------------'''
#ratioSeries2
def ratioSeries2(n):
    return ((n**2)+2*n+1)/((4*(n**2))+10*n+6)
#E2
def Ex2(L):#Applying the D'Alembert method
    #L==174, hence,|Rn|<=a(n+1)/1-L<eps
    bf=9/(2*mt.sqrt(3))
    a=1
    n=0
    sum=a
    a=ratioSeries2(n)*a
    for i in range(8,16):
        e = error(i)
        print "Erro "+str(e)+":"
        while (abs(a/(1-L))>e):
            n+=1
            sum+=a
            a=ratioSeries2(n)*a
        print "     |-n: "+str(n-1)
        print "     |-Sn: "+str(bf*sum)
    return
#Ex2 in Ex4
def Ex2n4():
    exact=mt.pi
    bf=9/(2*mt.sqrt(3))
    a=1
    sum=a
    Sn=bf*sum
    n=0
    for i in range(8,16):
        e = error(i)
        print "Erro "+str(e)+":"
        while (abs(exact-Sn)>e):
            a=ratioSeries2(n)*a
            n+=1
            sum+=a
            Sn=bf*sum
        print "     |-n: "+str(n)
        print "     |-Sn: "+str(bf*sum)
        print "     |-|S-Sn|: "+str(abs(exact-Sn))
    return

'''-----------------------------------------------------------------------------
                                Exercise 3/4
-----------------------------------------------------------------------------'''
#find N
def Ex3n4(exact):
    a=1
    n=0
    sum=a
    for i in range(8,16):
        e = error(i)
        print "Erro "+str(e)+":"
        while(abs(exact-4*sum)>e):
            n+=1
            a=((-1)**n)/(2*n+1)
            sum+=a
        print "     |-n: "+str(n)
        print "     |-Sn: "+str(4*sum)
        print "     |-|S-Sn|: "+str(abs(exact-4*sum))
    return
#Ex3
def Ex3():
    #|Rn|<|an+1|<e
    a=1
    n=0
    sum=a
    a=((-1)**(n+1))/(2*(n+1)+1)
    for i in range(8,16):
        e = error(i)
        print "Erro "+str(e)+":"
        while (abs(a)>e):
            n+=1
            sum+=a
            a=((-1)**n)/(2*n+1)
        print "     |-n: "+str(n-1)
        print "     |-Sn: "+str(sum)
    return
#Tests--------------------------------------------------------------------------
print "Exercicio 2:"
Ex2(1/4)
print "Exercicio 2 para exercicio 4"
Ex2n4()


print "Exercicio 3:"
Ex3()
#findN3(mt.pi)
print eps

#print somaUnica(2)
#somaTotal(eps)
