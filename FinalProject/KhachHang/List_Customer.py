from cgitb import reset
from hashlib import new
import re
from unittest import result
import KhachHang.Customer as cs 

class List_Customer:
    def __init__(self):
        self.list_customer  = list()
        
    
    def add_Customer(self):
        #tao Obj thuoc lop Product()
        new_customer = cs.Customer()
        new_customer.input_Customer()
        #them Obj vao list_Pro
        self.list_customer.append(new_customer)
        
    def add_All_Customer(self):
        n = input("Tao khach hang moi. Click Y. ")
        
        while n.upper() == "Y":
            self.add_Customer()
            print("Khoi tao khach thanh cong!")
            n = input("\n====> Tiep tuc tao them khach hang, click Y. ")
        else:
            isCreate_product = input("Dung viec tao khach hang moi! Click Y: ")
            if isCreate_product.upper() != "Y": #Tiep tuc tao sp
                print("\tTiep tuc tao san pham\n")
                self.add_All_Customer()
                #isCreate_product = input("Dung viec tao san pham moi! Click Y: ")
        
        #####Hien thi DS san pham
    def display_Customer(self):
        print("\n\tHIEN THI DANH SACH KHACH HANG\n")
        if len(self.list_customer) <=0:
            print(5*'*',"KHONG CO KHACH HANG NAO!", 5*'*')
        for i in range (0, len(self.list_customer)):
            self.list_customer[i].display_Cus_Info()
            
    def show_Customer(self):
        for i in self.list_customer:
            i.display_Cus_Info()
    
    def find_byCID(self):
        cID = input("Nhap ma can tim: ")
        for items in range (0, len(self.list_customer)):
            if self.list_customer[items].cid == cID:
                # print ("ID can tim: ", self.list_product[items].pname)
                # print("ID khong hop le")
                self.list_customer[items].display_Cus_Info()
                return [items, self.list_customer[items]]
        return False
    
    def remove_Customer(self):
        result = self.find_byCID()
        while result == False:
            print("Ma khach hang khong ton tai")
            self.find_byCID()
        else:
            self.list_customer.remove(result[1])
            print("\n=====>Xoa khach hang thanh cong.")
            self.display_Customer()
        
    def update_Customer(self):
        result  = self.find_byCID()
        while result == False:
            print("Khong tim thay Khach Hang!")
            self.find_byCID()
        else:
            result[1].cname = input("Nhap ten khach hang: ")
            
            self.show_Customer()
        pass      
            
    
# cus1 = List_Customer()
# cus1.list_customer
# cus1.add_All_Customer()
# #cus1.display_Customer()
# #cus1.update_Customer()
# cus1.remove_Customer()