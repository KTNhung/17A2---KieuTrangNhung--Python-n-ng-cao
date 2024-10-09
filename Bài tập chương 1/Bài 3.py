class Phanso:
    def __init__(self):
        self.tu = ""
        self.mau = ""
    def nhap(self):
        self.tu = int(input("Hãy nhập tử số: "))
        self.mau = int(input("Hãy nhập mẫu số:: "))
    def kiemtra(self):
        if self.mau == 0:
            return False
        else:
            return True
    def xuat(self):
        if(self.kiemtra()):
            print("Phần số là: ",self.tu,"/",self.mau)
        else:
            print("Phân số không hợp lệ!!!")
phanso1 = Phanso()
phanso1.nhap()
print(phanso1.kiemtra())
phanso1.xuat()