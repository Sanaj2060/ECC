from nPs import nPs
from addTwoPoints import addTwoPoints
from PointsFinder import psFinder
from ElGamal import ElGamal
from ecies import ecies
from findMulOrder import findmulorder
from primitiveRootsPro import proots
from SolveQR import qr
from millerRabin import millerRabinfunc
from fermatTest import fermatTest

if __name__ == "__main__":
    print("1. ADDITION TWO POINTS\n2. nPs\n3. Finding all the possible points (x,y) on a EC \
        \n4. Encryption and Decryption with ElGamal Method\
        \n5. Encryption and Decryption with ECIES Method\
        \n6. Find Orders of a  Multiplicative group\
        \n7. Primitive Roots\
        \n8. Quadratic Residue\
        \n9. Miller Rabin Test\
        \n10. Fermat Primality Test\
        \n\nEnter your choice: ")
    choice = int(input())
    #1 goes to def addTwoPoints
    if(choice == 1):
        print("----------------------------------------------------")
        print("Performing addition of two points:")
        print("----------------------------------------------------")
        powX = int(input("Power of X "))
        powY = int(input("Power of Y "))
        a = int(input('A: '))
        modBy = int(input("Mod By: "))
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))
        x2 = int(input('x2: '))
        y2 = int(input('y2: '))

        '''powX = 3
        powY = 2
        a = 1
        modBy = 11
        x1 = 2
        x2 = 5
        y1 = 7
        y2 = 9'''

        xNew, yNew = addTwoPoints(powX, powY, a, modBy, x1, y1, x2, y2)
        print(xNew, yNew)
    
    elif(choice == 2):
        print("----------------------------------------------------")
        print("Calculating the nPs:")
        print("----------------------------------------------------")
        n = int(input("Enter the value of n:"))
        powX = int(input("Power of X: "))
        powY = int(input("Power of Y: "))
        a = int(input('A: '))
        modBy = int(input("Mod By: "))
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))
        xNew, yNew = nPs(n, powX, powY, a, modBy, x1, y1)

        print("X: "+str(xNew)+", Y: "+str(yNew))
    
    elif(choice == 3):
        print("----------------------------------------------------")
        print("Finding all the points on a EC:")
        print("----------------------------------------------------")
        print(psFinder(), ", infinity")

    elif(choice == 4):
        print("----------------------------------------------------")
        print("Performing ELGAMAL:")
        print("----------------------------------------------------")
        ElGamal()

    elif(choice == 5):
        print("----------------------------------------------------")
        print("Performing ECIES:")
        print("----------------------------------------------------")
        ecies()
    
    elif(choice == 6):
        print("----------------------------------------------------")
        print("Calculating the order of Multiplicative group:")
        print("----------------------------------------------------")
        findmulorder()

    elif(choice == 7):
        print("----------------------------------------------------")
        print("Calculating the Primitive Roots:")
        print("----------------------------------------------------")
        proots()

    elif(choice == 8):
        print("----------------------------------------------------")
        print("Calculating the Quadratic Residue:")
        print("----------------------------------------------------")
        qr()

    elif(choice == 9):
        print("----------------------------------------------------")
        print("Performing Miller Rabin Test:")
        print("----------------------------------------------------")
        millerRabinfunc()

    elif(choice == 10):
        print("----------------------------------------------------")
        print("Performing Fermat Primality Test:")
        print("----------------------------------------------------")
        fermatTest()

    else:
        print("Please enter a Valid Choice!!")