class student:
    def __init__(self,n,r,pro,ram,hd,brand,cam):
        self.n=n
        self.r=r
        self.lap=self.laptop(pro,ram,hd)
        self.mob=self.mobile(brand,cam)
    def display(self):
        print(self.n,self.r)
        self.lap.display_lapy()
        self.mob.display_mobile()   
    class laptop:
        def __init__(self,pro,ram,hd):
            self.pro=pro
            self.ram=ram
            self.hd=hd
        def display_lapy(self):
            print("for lappy",self.pro,self.ram,self.hd)
    class mobile:
        def __init__(self,brand,cam):
            self.brand=brand
            self.cam=cam
        def display_mobile(self):
            print("for mobile",self.brand,self.cam)
std1=student("aravind",424,"i7","8gb","2tb","redmi","16px")
std1.display()
