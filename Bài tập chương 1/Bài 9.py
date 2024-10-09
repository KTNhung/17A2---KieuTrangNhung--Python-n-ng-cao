import math
class Dagiac:
    def __init__(self,canh):
        self.canh = canh
    def chu_vi(self):
        chuvi = 0
        for i in self.canh:
            chuvi = chuvi + i
        return chuvi
class hinhbinhhanh(Dagiac):
    def __init__(self, day, canhben, goc):
        super().__init__([day,canhben,day,canhben])
        self.day = day
        self.canhben = canhben
        self.chieucao = canhben*math.sin(goc)
    def dientich(self):
        return self.day*self.chieucao
class hinhchunhat(hinhbinhhanh):
    def __init__(self, dai, rong):
        super().__init__(dai,rong,math.pi/2)
class hinhvuong(hinhchunhat):
    def __init__(self, canh):
        super().__init__(canh,canh)
dg1 = Dagiac([2,3,4,2,1])
print("Cạnh đa giác:",dg1.canh)
print("Chu vi đa giác:",dg1.chu_vi())
hbh1 = hinhbinhhanh(10,5,math.pi/6)
print("Cạnh hình bình hành:",hbh1.canh)
print("Chu vi hình bình hành:",hbh1.chu_vi())
print("Diện tích hình bình hành:",hbh1.dientich())
hcn1 = hinhchunhat(10,5)
print("Cạnh chữ nhật:",hcn1.canh)
print("Chu vi hình chữ nhật:",hcn1.chu_vi())
print("Diện tích hình chữ nhật:",hcn1.dientich()) 
hv1 = hinhvuong(10)
print("Cạnh hình vuông:",hv1.canh)
print("Chu vi hình vuông:",hv1.chu_vi())
print("Diện tích hình vuông:",hv1.dientich())