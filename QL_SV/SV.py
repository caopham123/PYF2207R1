class SV:
    list_id = []
    def __init__(self):
        self.id   = ""
        self.name = ""
        self.major = ""
        self.address = ""
        self.age = 0
       
        
    def input_SV(self):
        print(len(self.list_id), self.list_id)
        
        self.id = input("Nhap ma SV: ")

        if self.id in self.list_id:
            print("\tSINH VIEN DA TON TAI!\n\tVui long nhap lai: ")
            self.id = input("Nhap ma SV: ")
        else:
            self.list_id.append(self.id)
            
        #Nhap thong tin khac
        self.name = input("Nhap ten: ")
        self.age = int(input("Nhap tuoi: "))
        self.address = (input("Nhap dia chi: "))
        self.major = (input("Nhap nganh: "))
       

    
    #Hien thi thong tin sp    
    def display_Info(self):
        print("id: {} ten: {} tuoi: {} nganh: {} D/c:{}".
              format(self.id, self.name, self.age, self.major, self.address))
        pass
    
    def update_Info(self):
        
        self.name = input("Nhap ten: ")
        self.age = int(input("Nhap tuoi: "))
        self.address = (input("Nhap dia chi: "))
        self.major = (input("Nhap nganh: "))
    

# pro1 = Product() 
# pro1.input_Product()
# pro1.display_Info()
       