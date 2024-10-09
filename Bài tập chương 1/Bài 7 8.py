class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    def display(self):
        print("Ngày:",self.day,"Tháng:",self.month,"Năm:",self.year)
    def next(self):
        m31 = [1,3,5,7,8,10]
        m30 = [4,6,9,11]
        if self.month == 12:
            if self.day == 31:
                self.year = self.year + 1
                self.month = 1
                self.day = 1
            else:
                self.day = self.day +1
        else:
            if self.month in m31:
                if self.day == 31:
                    self.month = self.month + 1
                    self.day = 1
                else:
                    self.day = self.day +1
            elif self.month in m30:
                if self.day == 30:
                    self.month = self.month + 1
                    self.day = 1
                else:
                    self.day = self.day + 1
            elif self.month == 2:
                if (self.year % 400 == 0) or ((self.year % 4 == 0) and (self.year % 100 != 0)):
                    if self.day == 29:
                        self.month = self.month + 1
                        self.day = 1
                    else:
                        self.day = self.day + 1
                else:
                    if self.day == 28:
                        self.month = self.month + 1
                        self.day = 1
                    else:
                        self.day = self.day + 1
QuocKhanh=Date(28,2,1948)
QuocKhanh.display()
QuocKhanh.next()
QuocKhanh.display()
class Employee(Date):
    def __init__(self, Ten, Birthday, Birthmonth, Birthyear, Joinday, Joinmonth, Joinyear):
        self.ten = Ten
        self.birthday = Date(Birthday, Birthmonth, Birthyear)
        self.joinday = Date(Joinday, Joinmonth, Joinyear)
Nhanvien1 = Employee("Nguyen Van A",1,10,2005,2,9,2024)
print(Nhanvien1.ten)
Nhanvien1.birthday.display()
Nhanvien1.joinday.display()