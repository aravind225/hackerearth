class Std:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print(self.name,self.roll,Std.clg)
    @classmethod
    def set_clge(self):
        Std.clg="sri"
        
m=Std("mur","4h3")
a=Std("ara",420)
a.set_clge()
a.display()
m.display()

        


