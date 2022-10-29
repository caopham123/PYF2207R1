class Product:
    list_pid = []
    def __init__(self):
        self.pid   = ""
        self.pname = ""
        self.price = 0
        self.discount = 0
        self.pnumber = 0
        self.bprice = 0
        #goi ham them thong tin sp
        #self.add_Product()
        #self.input_Product()
        
    def input_Product(self):
        #tao ds chua Pro_id
        
        print(len(self.list_pid), self.list_pid)
        
        self.pid = input("Nhap ma san pham: ")

        if self.pid in self.list_pid:
            print("\tSAN PHAM DA TON TAI!\n\tVui long nhap lai: ")
            self.pid   = input("Nhap ma san pham: ")
        else:
            self.list_pid.append(self.pid)
            
        #Nhap thong tin khac
        self.pname = input("Nhap ten san pham: ")
        self.price = float(input("Nhap gia san pham: "))
        self.pnumber = int(input("Nhap so luong san pham: "))
        self.bprice = self.price * self.pnumber
        # # self.discount = float(input("Nhap giam gia san pham: "))

    
    #Hien thi thong tin sp    
    def display_Info(self):
        print("id: {} tensp: {} gia: {} slg: {}".
              format(self.pid, self.pname, self.price,self.pnumber))
        pass
    
    def update_Info(self):
        
        self.pname = input("Cap nhat ten san pham: ")
    

# pro1 = Product() 
# pro1.input_Product()
# pro1.display_Info()
       