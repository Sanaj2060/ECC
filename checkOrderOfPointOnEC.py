from addTwoPoints import addTwoPoints

def copoec(powX, powY, a, modBy, x1, y1):
    xNew = x1
    yNew = y1
    i = 1
    while(True):
        if xNew == 0 and yNew == 0:
            print("The order of the Point %d,%d on the EC is: %d"%(x1,y1,i))
            break
        else:
            xNew, yNew = addTwoPoints(powX, powY, a, modBy, x1, y1, xNew, yNew)
    
        i+=1