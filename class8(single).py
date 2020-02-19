class car:
    tr=4
    def __init__(self,cc,power,mil,seats):
        self.cc=cc
        self.power=power
        self.mil=mil
        self.seats=seats
    def display(self):
        print(self.tr,self.power,self.mil,self.seats,self.cc)
class marathi(car):
    def __init__(self,ac,ab,cam,cc,power,mil,seats):
        super().__init__(cc,power,mil,seats)
        self.ac=ac
        self.ab=ab
        self.cam=cam
    def display_data(self):
        super().display()
        print(self.ac,self.ab,self.cam)
    def set_class_val(self,cc):
        self.cc=cc
swift=marathi("1","0","0","1500","20","21","5")
swift.display_data()
swift.set_class_val(1200)
swift.display_data()
