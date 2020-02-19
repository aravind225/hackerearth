""" inner class"""
class student:
    def __init__(self,n,roll):
        self.n=n
        self.roll=roll
    def display(self):
        print(self.n,self.roll)
    class laptop:
        def __init__(self,pro,ram,hd):
            self.pro=pro
            self.ram=ram
            self.hd=hd
        def display(self):
            print(self.pro,self.ram,self.hd)
std1=student("aravind",424)
std1.display()
lap=std1.laptop("i5","8GB","2GB")
lap.display()
