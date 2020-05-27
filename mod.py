from fractions import Fraction
from math import fmod

'''
Function to calculate mod operation
'''
def findMod(x, modBy, flag):
    res = 0
    #mod operation for integers
    if flag == 0:
        res = fmod(x, modBy)
        #for -ve mod
        if(res < 0 and res < modBy):
            res = res + modBy

    #mod operation for fractional values
    elif flag == 1:
        for i in range(1,modBy):
            #left hand side
            lhs = fmod(x.denominator * i, modBy)
            #for -ve mod
            if(lhs < 0 and lhs < modBy):
                lhs = lhs + modBy
            #right hand side
            rhs = fmod(x.numerator, modBy)
            #for -ve mod
            if(rhs < 0 and rhs < modBy):
                rhs = rhs + modBy
            #print(i, lhs, rhs)
            if(lhs == rhs):
                res = i
                break
    #print("res is ---------- "+str(res))
    return res

def modInverse(a, m) : 
	a = a % m 
	for x in range(1, m) : 
		if ((a * x) % m == 1) : 
			return x 
	return 1