from cgitb import reset
from hashlib import new
import re
from unittest import result
import QL_SV.SV as p

class List_SV:
    def __init__(self):
        self.list_sv  = list()
        
    
    def add_SV(self):
        #tao Obj thuoc lop Product()
        new_product = p.SV()
        new_product.input_SV()
        #them Obj vao list_Pro
        self.list_sv.append(new_product)
        
    def add_All_SV(self):
        n = input("Muon tao them SV, click Y. ")
        
        while n.upper() == "Y":
            self.add_SV()
            print("Khoi tao SV thanh cong!")
            n = input("\n====> Tiep tuc tao them SV, click Y. ")
        else:
            isCreate = input("Dung viec tao SV moi! Click Y: ")
            if isCreate.upper() != "Y": #Tiep tuc tao sp
                print("\tTiep tuc tao SV\n")
                self.add_All_SV()
                #isCreate = input("Dung viec tao san pham moi! Click Y: ")
        
        #####Hien thi DS san pham
    def display_SV(self):
        print("\n\tHIEN THI DANH SACH SV\n")
        if len(self.list_sv) <=0:
            print(5*'*',"KHONG CO SV NAO!", 5*'*')
        for i in range (0, len(self.list_sv)):
            self.list_sv[i].display_Info()
            
    def show_SV(self):
        for i in self.list_sv:
            i.display_Info()
    
    def find_byID(self):
        pID = input("Nhap ma can tim: ")
        for items in range (0, len(self.list_sv)):
            if self.list_sv[items].id == pID:
                self.list_sv[items].display_Info()
                return [items, self.list_sv[items]]
        return False
    
    def removed(self):
        result = self.find_byID()
        while result == False:
            print("Ma SV khong ton tai")
            self.find_byID()
        else:
            self.list_sv.remove(result[1])
            print("\n=====>Xoa SV thanh cong.")
            self.display_SV()
        
    def updated(self):
        result  = self.find_byID()
        while result == False:
            print("Khong tim thay SV!")
            self.find_byID()
        else:
            result[1].name = input("Nhap ten SV: ")
            result[1].age = int(input("Nhap tuoi SV: "))
            result[1].major = input("Nhap nganh SV: ")
            result[1].address = input("Nhap dia chi SV: ")
            
            self.show_SV()
             
list1 = List_SV()
list1.add_All_SV()
list1.display_SV
list1.find_byID()
list1.updated()
list1.removed()           
    
              
        
# list1 = list_sv()
# list1.add_All_Product()
# list1.display_SV()
# #list1.show_Product()
# #list1.find_byID()
# list1.removed()
# list1.updated()