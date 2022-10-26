from cgitb import reset
from hashlib import new
import re
from unittest import result
import QL_CT.Chitieu as p

class DS_ChiTieu:
    def __init__(self):
        self.ds_chitieu  = list()
        
    
    def add_Chitieu(self):
        #tao Obj thuoc lop Product()
        new_product = p.Chitieu()
        new_product.input_CT()
        #them Obj vao list_Pro
        self.ds_chitieu.append(new_product)
        
    def add_All_CT(self):
        n = input("Muon tao them Chi tieu, click Y. ")
        
        while n.upper() == "Y":
            self.add_Chitieu()
            print("Khoi tao Chi tieu thanh cong!")
            n = input("\n====> Tiep tuc tao them Chi tieu, click Y. ")
        else:
            isCreate = input("Dung viec tao Chi Tieu moi! Click Y: ")
            if isCreate.upper() != "Y": #Tiep tuc tao sp
                print("\tTiep tuc tao Chi tieu\n")
                self.add_All_CT()
                #isCreate = input("Dung viec tao san pham moi! Click Y: ")
        
        #####Hien thi DS san pham
    def display_CT(self):
        print("\n\tHIEN THI DANH SACH Chi Tieu\n")
        if len(self.ds_chitieu) <=0:
            print(5*'*',"KHONG CO Chi Tieu NAO!", 5*'*')
        for i in range (0, len(self.ds_chitieu)):
            self.ds_chitieu[i].display_Info()
            
    def show_ChiTieu(self):
        for i in self.ds_chitieu:
            i.display_Info()
    
    def find_CT(self):
        ten = input("Nhap chi tieu can tim: ")
        for items in range (0, len(self.ds_chitieu)):
            if self.ds_chitieu[items].name == ten:
                self.ds_chitieu[items].display_Info()
                return [items, self.ds_chitieu[items]]
        return False
    
    def removed(self):
        result = self.find_CT()
        while result == False:
            print("Ma Chi Tieu khong ton tai")
            self.find_CT()
        else:
            self.ds_chitieu.remove(result[1])
            print("\n=====>Xoa Chi Tieu thanh cong.")
            self.display_CT()
        
    def updated(self):
        result  = self.find_CT()
        while result == False:
            print("Khong tim thay Chi Tieu!")
            self.find_CT()
        else:
            result[1].name = input("Nhap ten Chi Tieu: ")
            result[1].val = float(input("Nhap gia tri Chi Tieu: "))
            result[1].day = input("Nhap ngay Chi Tieu: ")
            
            self.show_ChiTieu()
             
ds1 = DS_ChiTieu()
ds1.add_All_CT()
ds1.display_CT()

ds1.removed()

              
        
# list1 = ds_chitieu()
# list1.add_All_Product()
# list1.display_Chi Tieu()
# #list1.show_Product()
# #list1.find_byID()
# list1.removed()
# list1.updated()