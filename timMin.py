import array as arr


def taoMang():
    number = int(input("Nhap so phan tu: "))
    arr1 = []
    for i in range (number):
        item = int(input("Nhap phan tu {}: ".format(i)))
        arr1.append(int(item))
        
    return number, arr1

def xuatMang(n, Arr1):      
    for i in range (n):
        print('A[{}] = {}'.format(i, Arr1[i]))
  
def tim_Min(n,Arr1):
    minVal = Arr1[0]
    for  i in range(1,n):
        if(minVal > Arr1[i]):
            minVal = Arr1[i]
    return minVal

def Main():
    n,arr = taoMang()
    xuatMang(n,arr)
    rs = tim_Min(n,arr)
    print("Gia tri nho nhat la {}:".format(rs))
Main()