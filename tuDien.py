#%%
my_dict = {
    'hi': ('chao', 'xin chao'),
    'eat': 'an',
    'drink': 'uong',
    'drive': {'lai xe', 'chay xe'}
}
# print(my_dict.keys())
# print(my_dict.get('hi'))

def input_key ():
    keyword = input("Nhap tu can dich. Neu khong, chon '0':  ")
    while True:
        if keyword == '0':
            break
        elif keyword not in my_dict.keys():
            print("======>'{}' khong co trong TU DIEN!".format(keyword))
            keyword = input("Nhap tu can dich: ")
        else:
            print( "{} ".format(my_dict.get(keyword)) )
            keyword = input("Nhap tu can dich: ")
        
input_key()
            
        
    