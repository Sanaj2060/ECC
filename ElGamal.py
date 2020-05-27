from nPs import nPs
from addTwoPoints import addTwoPoints

'''Encryption and Decryption using ElGamal Method'''

def ElGamal():
    powX = int(input("Power of X: "))
    powY = int(input("Power of Y: "))
    a = int(input('A: '))
    modBy = int(input("Mod By: "))
    senderSecretKey = int(input("Enter Sender Secret Key: "))
    recieverSecretKey = int(input("Enter Sender Reciever Key: "))
    publicPointX = int(input("Enter Public Point X: ")) 
    publicPointY = int(input("Enter Public Point Y: "))
    msgNo = int(input("Enter the Number of msgs to be encrypted: "))

    #Need to write proper for loop - note TO SELF
    msg = [[int(input("Enter the msgs: ")) for _ in range(2)] for _ in range(msgNo)]
    print(msg)

    for i in range(msgNo):
        currMsg = msg[i]
        mOneX, mOneY = nPs(senderSecretKey, powX, powY, a, modBy, publicPointX, publicPointY)
        bX, bY = nPs(recieverSecretKey, powX, powY, a, modBy, publicPointX, publicPointY)
        kBX, kBY = nPs(senderSecretKey, powX, powY, a, modBy, bX, bY)
        
        mTwoX, mTwoY = addTwoPoints(powX, powY, a, modBy, currMsg[0], currMsg[1], kBX, kBY)

        encryptedMsg = [[mOneX, mOneY],[mTwoX, mTwoY]]
        print("The encrypted Msg for:",currMsg," is: ",encryptedMsg)

        choice = int(input("To Continue with Decryption enter 1: "))
        if choice == 1:
            ElGamalDecryption(powX, powY, a, modBy, mTwoX, mTwoY, mOneX, mOneY, recieverSecretKey)

#DECRYPTION PART (OPTIONAL)
def ElGamalDecryption(powX, powY, a, modBy, mTwoX, mTwoY, mOneX, mOneY, recieverSecretKey):
    smOneX, smOneY = nPs(recieverSecretKey, powX, powY, a, modBy, mOneX, mOneY)
    #to get the inverse of point (smOnex, smOneY), which is equal to (smOneX, -smOneY(mod modBy))
    # point (x,y) and point (x,-y), which is equal to point (x,p-y) 
    smOneY = modBy - smOneY

    msgX, msgY = addTwoPoints(powX, powY, a, modBy, mTwoX, mTwoY, smOneX, smOneY)
    decryptedMsg = [msgX, msgY]
    print("The Decrypted msg is: ", decryptedMsg) 



