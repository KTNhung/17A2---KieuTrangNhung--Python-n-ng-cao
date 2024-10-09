class Stack:
    def __init__(self,len):
        self.stack = []
        self.len = len
    def push(self,x):
        if not self.isFull():
            self.stack.append(x)
            print("Push:",x,"vào stack")
        else:
            print("Stack đã đầy!!!")
    def pop(self):
        if not  self.isEmty():
            x = self.stack.pop()
            print("Pop:",x,"khỏi stack")
        else:
            print("Stack đã rổng")
    def isEmty(self):
        if len(self.stack) == 0:
            return True
    def isFull(self):
        if len(self.stack) == self.len:
            return True
    def count(self):
        return len(self.stack)
    def xuat(self):
        print("Stack hiện tại: ",self.stack[::-1])
stack1 = Stack(5)
stack1.pop()

stack1.push(5)
stack1.push(6)
stack1.push(8)
stack1.push(9)
stack1.push(10)
stack1.push(5)

stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()

stack1.push(8)
stack1.push(9)
stack1.push(10)
print("Số phần tử của stack là:",stack1.count())
stack1.xuat()