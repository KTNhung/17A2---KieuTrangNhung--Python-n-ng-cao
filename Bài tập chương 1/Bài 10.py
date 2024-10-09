import math
class diem:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class elip(diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.bankinhchinh = a
        self.bankinhphu = b
    def dientich(self):
        return math.pi*self.bankinhchinh*self.bankinhphu
class duongtron(elip):
    def __init__(self,x ,y, r):
        super().__init__(x,y,r,r)
diemA = diem(5,10)
print("Tọa độ điểm là:",diemA.x,diemA.y)
Elip1 = elip(5,10,20,30)
print("Tọa độ tâm của elip là:",Elip1.x,Elip1.y)
print("Bán kính chính của Elip là:",Elip1.bankinhchinh)
print("Bán kính phụ của Elip là:",Elip1.bankinhphu)
print("Diện tích của elip là:",Elip1.dientich())
dtron = duongtron(1,2,10)
print("Tọa độ tâm đường tròn là:",dtron.x,dtron.y)
print("Bán kính đường tròn là: ",dtron.bankinhchinh)
print("Diện tích đường tròn là", dtron.dientich())