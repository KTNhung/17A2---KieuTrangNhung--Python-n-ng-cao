class HCN:
    def __init__(self):
        self.chieudai = int(input("Hãy nhập chiều dài: "))
        self.chieurong = int(input("Hãy nhập chiều rộng: "))
        self.chuvi = (self.chieudai + self.chieurong)*2
        self.dientich = self.chieudai * self.chieurong
    def show(self):
        print("Chiều dài hình chữ nhật là: {}\nChiều rộng hình chữ nhật là: {}\nChu vi hình chữ nhật là: {}\nDiện tích hình chữ nhật là: {}".format(self.chieudai,self.chieurong,self.chuvi,self.dientich))
HCN1 = HCN()
print(HCN1.show())
