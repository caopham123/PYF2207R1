class Chitieu:
    def __init__(self):
        self.name = ""
        self.val = 0
        self.day = ""
        
    def input_CT(self):
            
        #Nhap thong tin khac
        self.name = input("Nhap ten: ")
        self.val = float(input("Nhap gia tri: "))
        self.day = (input("Nhap ngay: "))
    
    #Hien thi thong tin sp    
    def display_Info(self):
        print("ten: {}   gia tri: {}    ngay: {}".
              format(self.name, self.val, self.day))
        pass
    
    def update_Info(self):
        self.name = input("Nhap ten: ")
        self.val = float(input("Nhap gia tri: "))
        self.day = (input("Nhap ngay: "))
    

# pro1 = Product() 
# pro1.input_Product()
# pro1.display_Info()
       