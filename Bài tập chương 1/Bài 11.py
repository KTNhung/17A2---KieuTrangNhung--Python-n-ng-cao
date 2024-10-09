import math
class tamgiac:
    def __init__(self,canh1,canh2,canh3):
            self.canh1 = canh1
            self.canh2 = canh2
            self.canh3 = canh3
            if self.canh1 + self.canh2 < self.canh3 and self.canh1 > self.canh2 + self.canh3 and self.canh3 + self.canh1 < self.canh2:
                self.canh1 = None
                self.canh2 = None
                self.canh3 = None
                print("Đây không phải tam giác")
class tamgiacvuong(tamgiac):
    def __init__(self,canhgv1,canhgv2):
        super().__init__(canhgv1,canhgv2,math.sqrt(canhgv1**2+canhgv2**2))
class tamgiaccan(tamgiac):
    def __init__(self, canh1, canh2):
        super().__init__(canh1, canh1, canh2)
class tamgiacdeu(tamgiaccan):
    def __init__(self, canh1):
        super().__init__(canh1, canh1)
tg1 = tamgiac(5,2,4)
tgv1 = tamgiacvuong(3,4)
tgc1 = tamgiaccan(3,4)
tgd1 = tamgiacdeu(3)
print("3 Cạnh của tam giác là: ",tg1.canh1,tg1.canh2,tg1.canh3)
print("3 Cạnh của tam vuông là: ",tgv1.canh1,tgv1.canh2,tgv1.canh3)
print("3 Cạnh của tam cân là: ",tgc1.canh1,tgc1.canh2,tgc1.canh3)
print("3 Cạnh của tam đều là: ",tgd1.canh1,tgd1.canh2,tgd1.canh3)