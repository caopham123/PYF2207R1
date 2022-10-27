from cgitb import reset
from hashlib import new
import re
from unittest import result
import QL_Sanpham.Product as p 

class List_Product:
    def __init__(self):
        self.list_product  = list()
        
    
    def add_Product(self):
        #tao Obj thuoc lop Product()
        new_product = p.Product()
        new_product.input_Product()
        #them Obj vao list_Pro
        self.list_product.append(new_product)
        
    def add_All_Product(self):
        n = input("Muon tao them sp, click Y. ")
        
        while n.upper() == "Y":
            self.add_Product()
            print("Khoi tao san pham thanh cong!")
            n = input("\n====> Tiep tuc tao them sp, click Y. ")
        else:
            isCreate_product = input("Dung viec tao san pham moi! Click Y: ")
            if isCreate_product.upper() != "Y": #Tiep tuc tao sp
                print("\tTiep tuc tao san pham\n")
                self.add_All_Product()
                #isCreate_product = input("Dung viec tao san pham moi! Click Y: ")
        
        #####Hien thi DS san pham
    def display_Product(self):
        print("\n\tHIEN THI DANH SACH SAN PHAM\n")
        if len(self.list_product) <=0:
            print(5*'*',"KHONG CO SAN PHAM NAO!", 5*'*')
        for i in range (0, len(self.list_product)):
            self.list_product[i].display_Info()
            
    def show_Product(self):
        for i in self.list_product:
            i.display_Info()
    
    def find_byID(self):
        pID = input("Nhap ma can tim: ")
        for items in range (0, len(self.list_product)):
            if self.list_product[items].pid == pID:
                # print ("ID can tim: ", self.list_product[items].pname)
                # print("ID khong hop le")
                self.list_product[items].display_Info()
                return [items, self.list_product[items]]
        return False
    
    def remove_Product(self):
        result = self.find_byID()
        while result == False:
            print("Ma san pham khong ton tai")
            self.find_byID()
        else:
            self.list_product.remove(result[1])
            print("\n=====>Xoa san pham thanh cong.")
            self.display_Product()
        
    def update_Product(self):
        result  = self.find_byID()
        while result == False:
            print("Khong tim thay san pham!")
            self.find_byID()
        else:
            result[1].pname = input("Nhap ten san pham: ")
            
            self.show_Product()
             
            
    
              
        
# list1 = List_Product()
# list1.add_All_Product()
# list1.display_Product()
# #list1.show_Product()
# #list1.find_byID()
# list1.remove_Product()
# list1.update_Product()