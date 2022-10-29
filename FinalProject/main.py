import QL_Sanpham.Product as p  
import QL_Sanpham.List_Product as l 
import KhachHang.Customer as cs
import KhachHang.List_Customer as lcs
import HoaDon.Bills as bill

class Main:
    list1 = l.List_Product()
    list2 = lcs.List_Customer()
    list3 = bill.Bills()

    def Menu_Product(self):
            print(50*'=',end='\n')
            print("\n\tQUAN LY SAN PHAM!!!\n")
            print("\t 1. Hien thi danh sach san pham.")
            print("\t 2. Them san pham.")
            print("\t 3. Cap nhat thong tin san pham")
            print("\t 4. Xoa san pham.")
            print("\t 5. Tim kiem theo ID")
            print("\t 0. Thoat")
            print(50*'=',end='\n\n')
            
    def Menu_Customer(self):
        print(50*'=',end='\n')
        print("\n\tQUAN LY KHACH HANG!!!\n")
        print("\t 1. Hien thi danh sach khach hang.")
        print("\t 2. Them khach hang.")
        print("\t 3. Cap nhat thong tin khach hang")
        print("\t 4. Xoa khach hang.")
        print("\t 5. Tim kiem theo ID")
        print("\t 0. Thoat")
        print(50*'=',end='\n\n')
    
    # def Menu_Bill(self):
    #     print(50*'=',end='\n')
    #     print("\n\tQUAN LY HOA DON!!!\n")
    #     print("\t 1. Hien thi hoa don nhap.")
    #     print("\t 2. Them hoa don.")
    #     # print("\t 3. Cap nhat thong tin khach hang")
    #     # print("\t 4. Xoa khach hang.")
    #     # print("\t 5. Tim kiem theo ID")
    #     print("\t 0. Thoat")
    #     print(50*'=',end='\n\n')
        

    def Selected_Product(self):
        my_selection = int(input("===>Chon chuc nang tu 0 - 6: "))
    
        while my_selection >=0:
            if my_selection == 1:
                self.list1.display_Product()
                break
            elif my_selection == 2:
                self.list1.add_All_Product()
                break
            elif my_selection == 3:
                self.list1.update_Product()
                break
            elif my_selection == 4:
                self.list1.remove_Product()
                break
            elif my_selection == 5:
                self.list1.find_byID()
                break
            elif my_selection == 0:
                break

    def Selected_Customer(self):
        
        my_selection = int(input("===>Chon chuc nang tu 0 - 6: "))
    
        while my_selection >=0:
            if my_selection == 1:
                self.list2.display_Customer()
                break
            elif my_selection == 2:
                self.list2.add_All_Customer()
                break
            elif my_selection == 3:
                self.list2.update_Customer()
                break
            elif my_selection == 4:
                self.list2.remove_Customer
                break
            elif my_selection == 5:
                self.list2.find_byCID()
                break
            elif my_selection == 0:
                break

    # def Selected_Bill(self):
    #     my_selection = int(input("===>Chon chuc nang tu 0 - 6: "))
        
    #     while my_selection >=0 and my_selection <=6:
    #         if my_selection == 1:
    #             self.list3.display_Bill()
    #             break
    #         elif my_selection == 2:
    #             self.list3.insert_Next_Product(self.list1)
    #             break
    #         else:
    #             break
            
    def Main(self):
        while True: 
            print(50*"=",end='\n')
            print("\t 1. QUAN LY SAN PHAM.")
            print("\t 2. QUAN LY KHACH HANG.")
            #  
            print("\t 0. THOAT")
            print(50*'=',end='\n\n')
            
            my_selection = int(input("===> Chon chuc nang Quan ly: "))
            
            while my_selection == 1:
                self.Menu_Product()
                self.Selected_Product()
                # self.Menu_Bill()
                # self.Selected_Bill()
                my_selection = int(input("===> \nChon chuc nang Quan ly: "))
                
            while my_selection == 2:
                self.Menu_Customer()
                self.Selected_Customer()
                my_selection = int(input("\n===>Chon chuc nang Quan ly: "))
            else: 
                break 
a = Main()
a.Main()
