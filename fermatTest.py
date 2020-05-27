import random

def power(a, n, p):
    res = 1
    a = a % p

    while(n > 0):
        #if n is odd, multiply 'a' with res
        if((n & 1) == 1):
            res = (res * a) % p

        #n must be even now
        n = n >> 1
        a = (a * a) % p

    return res


def isPrime(n,k):
    #corner cases
    if n <= 1 or n == 4:
        return False
    elif n <= 3:
        return True

    #try K times
    while(k > 0):
        #pick a random number in [2..n-2]
        #Above corner cases make sure that n > 4
        a = 2 + (int(random.random()) % (n - 4))

        # Fermat's little Theorem
        if power(a, n-1, n) != 1:
            return False

        k -= 1

    return True

def fermatTest():
    k = 3
    n = int(input("Enter the Number you want to check: "))
    if isPrime(n,k):
        print("PASS")
    else:
        print("FAIL")