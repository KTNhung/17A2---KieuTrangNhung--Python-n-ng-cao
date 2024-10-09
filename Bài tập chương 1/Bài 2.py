class Sinhvien:
    def __init__(self):
        self.ten = ""
        self.diemtoan = ""
        self.diemly = ""
        self.diemhoa = ""
    def nhap(self):
        self.ten = input("Hãy nhập họ và tên: ")
        self.diemtoan = int(input("Hãy nhập điểm toán: "))
        self.diemly = int(input("Hãy nhập điểm lý: "))
        self.diemhoa = int(input("Hãy nhập điểm hóa: "))
    def xuat(self):
        print("Sinh viên có tên là: {}\nSinh viên có điểm toán là: {}\nSinh viên có điểm lý là: {}\nSinh viên có điểm hóa là: {}".format(self.ten,self.diemtoan,self.diemly,self.diemhoa))
    def tong(self):
        return self.diemly + self.diemtoan + self.diemhoa
n = int(input("So sinh vien ban muon nhap: "))
ListSV = []
for i in range(n):
    temp = Sinhvien()
    temp.nhap()
    ListSV.append(temp)
for i in range(0,len(ListSV)):
    max = ListSV[i].tong()
    for j in range(i,len(ListSV)):
        if max < ListSV[j].tong():
            temp = ListSV[i]
            ListSV[i] = ListSV[j]
            ListSV[j] = temp
            max = ListSV[j].tong()
print("Danh sach sinh vien trung tuyen: ")
for i in ListSV:
    if i.tong() < 20:
        break
print("Ten",i.ten,"\tDiem",i.tong())