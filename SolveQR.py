from math import fmod

def checkQR(powX, a, p):
    flag = 0
    for i in range(1, p, 1):
        if fmod(i**powX, p) == fmod(a,p):
            #qrList.append(i)
            flag = 1
            break
    return i, flag

def findAllQR(powX, p):
    qrList = []
    for i in range(1, p, 1):
        temp, checkQRres = checkQR(powX, i, p)
        if checkQRres == 1:
            qrList.append(i)

    return qrList


def qr():
    powX = int(input("Enter the power of X: "))
    #a = int((input("Enter a of x^powX = a mod p: ")))
    p = int((input("Enter p of x^powX = a mod p: ")))

    qrs = findAllQR(powX, p)
    print(qrs)

    var = int(input("Enter the number to check if it is a QR of %d: "%p))
    temp, checkQRres = checkQR(powX, var, p)
    if checkQRres == 1:
        print("%d is a QR of mod %d at x = %d"%(var,p,temp))
    else:
        print("%d is a NON-QR of mod %d"%(var,p))

