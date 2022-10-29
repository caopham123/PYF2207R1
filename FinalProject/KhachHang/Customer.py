class Customer:
    list_cid = []
    def __init__(self):
        self.cid   = ""
        self.cname = ""
        
        
    def input_Customer(self):
        #tao ds chua Pro_id
        
        print(len(self.list_cid), self.list_cid)
        
        self.cid = input("Nhap ma khach hang: ")

        if self.cid in self.list_cid:
            print("\tSAN PHAM DA TON TAI!\n\tVui long nhap lai: ")
            self.cid   = input("Nhap ma khach hang: ")
        else:
            self.list_cid.append(self.cid)
            
        #Nhap thong tin khac
        self.cname = input("Nhap ten khach hang: ")
        
    
    #Hien thi thong tin sp    
    def display_Cus_Info(self):
        print("id: {} khach hang: {}".format(self.cid, self.cname))
        pass
    
    def update_Cus_Info(self):
        
        self.cname = input("Cap nhat ten khach hang: ")
    

# pro1 = Product() 
# pro1.input_Product()
# pro1.display_Info()
       