from fractions import Fraction
from math import fmod
from mod import findMod

'''Addition of Two Points of an EC'''
def addTwoPoints(powX, powY, a, modBy, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        #Calculating Lambda
        ld_temp_up = (powX*(x1**(powX-1))+a)
        ld_temp_down = (powY*(y1**(powY-1)))
        #check if ld_temp_up divides ld_temp_down
        if (ld_temp_up % ld_temp_down == 0):
            flag = 0
            ld_temp = ld_temp_up/ld_temp_down
            #print("The ld_temp from case 1 is:"+str(ld_temp))
        else:
            flag = 1
            #Converting to intType bcoz Fraction() doesn't accept float values
            ld_temp_up = int(fmod(ld_temp_up, modBy))
            ld_temp_down = int(fmod(ld_temp_down, modBy))
            #Converting into rational number
            ld_temp = Fraction(ld_temp_up, ld_temp_down)
            #print("The ld_temp from case 2 is:"+str(ld_temp))
        
        #print("The ld_temp to be sent is:"+str(ld_temp))
        ld = findMod(ld_temp, modBy, flag)
        #print("The Lambda is: "+str(ld))

        #calculating the xNew and yNew
        xNew = (ld**2) - x1 -x2
        xNew = findMod(xNew, modBy, flag=0)
        yNew = ld*(x1 - xNew) - y1
        yNew = findMod(yNew, modBy, flag=0)
        
        return (xNew,yNew)

    else:
        ld_temp_up = (y2 - y1)
        ld_temp_down = (x2 - x1)

        if (ld_temp_up % ld_temp_down == 0):
            flag = 0
            ld_temp = ld_temp_up/ld_temp_down
            #print("The ld_temp from case 1 is:"+str(ld_temp))
        else:
            flag = 1
            ld_temp_up = int(fmod(ld_temp_up, modBy))
            #print("ld_temp_up: "+str(ld_temp_up))
            ld_temp_down = int(fmod(ld_temp_down, modBy))
            #print("ld_temp_down: "+str(ld_temp_down))
            ld_temp = Fraction(ld_temp_up, ld_temp_down)
            #print("The ld_temp from case 2 is:"+str(ld_temp))
        
        #print("The ld_temp to be sent is:"+str(ld_temp))
        ld = findMod(ld_temp, modBy, flag)
        #print("x1 != x2 The Lambda is: "+str(ld))
        xNew = (ld**2) - x1 -x2
        xNew = findMod(xNew, modBy, flag=0)
        yNew = ld*(x1 - xNew) - y1
        yNew = findMod(yNew, modBy, flag=0)
        
        return (xNew,yNew)