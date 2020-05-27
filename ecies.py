from nPs import nPs
from math import fmod, sqrt
from mod import findMod, modInverse
'''Encryption and decryption using ECIES Method'''

def ecies():
    powX = int(input("Power of X: "))
    powY = int(input("Power of Y: "))
    a = int(input('A: '))
    b = int(input('B: '))
    modBy = int(input("Mod By: "))
    senderSecretKey = int(input("Enter Sender Secret Key: "))
    recieverSecretKey = int(input("Enter Sender Reciever Key: "))
    publicPointX = int(input("Enter Public Point X: ")) 
    publicPointY = int(input("Enter Public Point Y: "))
    msg = int(input("Enter the Msg to be Encrypted: "))

    #Computing Q 
    qX, qY = nPs(recieverSecretKey, powX, powY, a, modBy, publicPointX, publicPointY)
    #Computing kP
    kPX, kPY = nPs(senderSecretKey, powX, powY, a, modBy, publicPointX, publicPointY)
    #Computing kQ
    kQX, kQY = nPs(senderSecretKey, powX, powY, a, modBy, qX, qY)

    #p = modBy is odd prime, if y is an odd number, then p-y is an even number and vice versa.
    #Hence, we can compress point (x,y) by (x, y mod 2), of which the possible result is (x,0) or (x,1)
    #For more: https://bit.ly/3bYT7Ic

    #Checking for QUADRATIC RESIDUE
    for i in range(1,int(((modBy-1)/2) + 1)):
        if (i ** 2) % modBy == kPY:
            QR = 1

    if (QR == 1):
        compressedX = kPX
        compressedY = fmod(kPY, 2)
    
    else:
        compressedX = kPX
        compressedY = kPY/sqrt(2)
        compressedY = fmod(compressedY, 2)

    #CipherText = ((x1, y1),y3) and y3 = x2 * x (mod modBy), where x is the original msg
    yThree = findMod((kQX * msg), modBy, flag=0)
    cipherText = [[compressedX, compressedY],[yThree, 0]]

    print("The Encrypted msg is: ",cipherText)
    #for decryption
    choice = int(input("To Continue to the Decryption part enter 1: "))

    if choice == 1:
        eciesDecryption(cipherText, recieverSecretKey, powX, powY, a, b, modBy)

def eciesDecryption(cipherText, recieverSecretKey, powX, powY, a, b, modBy):
    #decompression of points
    #https://bit.ly/2X2Vnu1 - Page 66 - Fig. 2
    temp = findMod((cipherText[0][0] ** powX + cipherText[0][0] * a + b), modBy, flag=0)
    dY = sqrt(temp)

    if findMod(dY, 2, flag=0) != cipherText[0][1]:
        dY = (-1) * dY

    dX = cipherText[0][0]

    #computing sKP
    sKPX, sKPY = nPs(recieverSecretKey, powX, powY, a, modBy, dX, dY)

    msg = findMod((cipherText[1][0] * modInverse(sKPX, modBy)), modBy, flag=0)
    print("The Original MSG is: ",msg)