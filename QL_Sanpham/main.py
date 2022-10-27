import QL_Sanpham.Product as p  
import QL_Sanpham.List_Product as l 

class Main:
    list1 = l.List_Product()
   

    def Menu_Product(self):
            print(50*'=',end='\n')
            print("\n\tQUAN LY SAN PHAM!!!\n")
            print("\t 1. Them san pham.")
            print("\t 2. Cap nhat thong tin san pham")
            print("\t 3. Xoa san pham.")
            print("\t 4. THOAT.")
            print("\t 5. Tim kiem theo ID")
            print("\t 6. Hien thi SP")
            print(50*'=',end='\n\n')
            

    def Selected_Product(self):
        my_selection = int(input("===>Chon chuc nang tu 0 - 6: "))
    
        while my_selection >=6:
            if my_selection == 0:
                self.list1.display_Product()
                break
            elif my_selection == 1:
                self.list1.add_All_Product()
                break
            elif my_selection == 2:
                self.list1.update_Product()
                break
            elif my_selection == 3:
                self.list1.remove_Product()
                break
            elif my_selection == 5:
                self.list1.find_byID()
                break
            elif my_selection == 4:
                break

    def Main(self):
        while True: 
            
            self.Menu_Product()
            self.Selected_Product()
            
a = Main()
a.Main()
