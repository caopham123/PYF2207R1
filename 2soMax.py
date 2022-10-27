list1 = [10,-20,15,60,3,40]

def find_Max(my_list):
    maxVal = my_list[0]
    vitri = 0
    for i in range (0, len(my_list)):
        if (maxVal < my_list[i]):
            maxVal = my_list[i]
            vitri = i
    print("Vi tri i= {} co gia tri lon nhat {}".format(vitri, maxVal))
    # new_list = my_list.copy().pop(vitri) 
    new_list = my_list.pop(vitri)
    return new_list
    
def Main():
    num = int(input("Nhap so luong vi tri lon nhat can tim: "))
    copied_list = list1.copy()
    rs = []
    for i in range (0,num):
        rs.append(find_Max(copied_list))
        copied_list = copied_list.copy()
    
    print(rs)
Main()