def nhap_3_So():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))
    
    return x,y,z

def sap_Xep(x,y,z):
    maxVal = x
    if(y>=maxVal):
        maxVal = y
        if(z>= maxVal):
            maxVal = z
    
    else:
        if (z>= maxVal):
            maxVal = z
    return maxVal

def Main():
    x,y,z = nhap_3_So()
    rs = sap_Xep(x,y,z)
    print("Gia tri lon nhat la {}".format(rs))
    
Main()