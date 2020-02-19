from abc import ABC,abstractmethod

class a(ABC):
    def __init__(self):
        print("superclass")
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def setvalues(self):
        pass
class b(a):
    def __init__(self):
        super().__init__()
        print("sub class")
    def display(self):
        print("abstract display method")
    def setvalues(self):
        print("abstract setvalues")
obj=b()
