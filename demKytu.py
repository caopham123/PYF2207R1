def nhap_chuoi():
    my_str = input("Nhap chuoi: ")
    
    return my_str
ChuSo = [1,2,3,4,5,6,7,8,9,0]

def dem_Kytu(my_str):
    count = 0
    count_num = 0
    for char in my_str:
        count +=1
        
    print('Chuoi co {} ky tu'.format(count))
    

def Main():
    my_str= nhap_chuoi()
    dem_Kytu(my_str)
    
Main()