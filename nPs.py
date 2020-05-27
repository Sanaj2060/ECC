from addTwoPoints import addTwoPoints

def nPs(n, powX, powY, a, modBy, x1, y1):
    xNew = x1
    yNew = y1
    for i in range(0, n-1):
            xNew, yNew = addTwoPoints(powX, powY, a, modBy, x1, y1, xNew, yNew)
            #print(xNew, yNew)

    return xNew, yNew