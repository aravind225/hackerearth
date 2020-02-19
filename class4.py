class college:
    under_university="jntuk"
    def __init__(self,courses,blockscount,phnumber,clsroomscount,clgname):
        self.courses=courses
        self.bc=blockscount
        self.phno=phnumber
        self.clsc=clsroomscount
        self.clgname=clgname
    @classmethod
    def set_college(cls,n):
        cls.under_university=n
    def display(self):
        return self.courses,self.bc,self.phno,self.clsc,self.clgname,college.under_university
clg1=college("btech",3,9393939393,105,"Aditya")
clg2=college("diplomo",2,664665757,56,"Sri Aditya")

print(clg1.display())
clg1.set_college("AU")
print(clg1.display())
print(clg2.display())
