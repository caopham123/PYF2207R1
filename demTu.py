list_chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "   wellcom to lap   kho trinh khong   kho  qua kho "

def xoa_khoang_trang(my_string):
    my_string = my_string.strip()
    while '  ' in my_string:
        my_string = my_string.replace('  ', ' ')
    return my_string

def count_Words(my_string):
    test_str = input("Nhap chuoi can dem: ")
    sub_string = my_string.split(' ')
    print(sub_string, end='\n')
    count = 0
    # if test_str not in sub_string:
    #     print("'{}'  khong co trong DS".format(test_str))
    #     print('Nhap lai: ')
    for i in sub_string:
        if test_str == i:
            count +=1
        # else: count =1
        
    print("'{}' xuat hien {} lan".format(test_str, count))

check_string = xoa_khoang_trang(check_string)
print(check_string)
count_Words(check_string)

            
    
    
    

    
# sub_string = check_string.split(' ')
# print(sub_string, sep='; ')
# kytu = 'l'
# dem = check_string.count(kytu)
# print("{}: {} lan".format(kytu, dem))
# for char in chars:
#       count = check_string.count(char)
#   if count > 1:
#     print(char, count)
 