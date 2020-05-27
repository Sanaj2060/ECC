from mod import findMod

'''Finding of all sets of (x,y) on a EC'''

#for Sorting key
def sortX(val): 
    return val[0] 

def psFinder():
    powX = int(input("Power of X: "))
    powY = int(input("Power of Y: "))
    a = int(input("A: "))
    b = int(input("B: "))
    modBy = int(input("Mod By: "))

    posYsq = set()  
    xAndrhs = []

    for i in range(0, modBy):
        rhs = findMod((i**powX + a*i + b), modBy, flag=0)
        #adding possible values of y^2
        posYsq.add(rhs)
        xAndrhs.insert(i,[i,rhs])
        #print(xAndrhs[i][0], xAndrhs[i][1])
        #print("When x = %d => RHS = %d", i,rhs)
    #print(posYsq)
    #print(xAndrhs)

    #finding the x and y
    counter = 0
    points = []
    for  i in range(0, modBy):
        #checking if y^2 mod modBy is in Possible values of y^2
        if findMod(i**powY, modBy, flag=0) in posYsq:
            #if YES, get the value of x and y
            for j in range(len(xAndrhs)):
                if(xAndrhs[j][1] == findMod(i**powY, modBy, flag=0)):
                    #print(xAndrhs[j][0], i)
                    points.insert(counter,[xAndrhs[j][0],i])
                    counter+=1
    points.sort(key = sortX)
    return points