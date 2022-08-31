#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 
#Inner class 
#Example of create obj of inner class outside of the outer class 
#comparing with other inner class exmaple, why one is best to use? is it depdned on design situation?


class Student:   #outer class

    def __init__(self, name, rollno):
        self.name = name 
        self.rollno = rollno 
        self.lap = self.Laptop()  # step 3; create obj

    def show(self): #this show() response to outside class only
        print(self.name, self.rollno)   
        self.lap.show()       ###


    class Laptop:     #step 1   inner class
        def __init__(self):
            self.brand = "HP"
            self.cpu = "Intel i5"
            self.RAM = "Hynix DDR4 64GM RDIMM"
        
        def show(self):  #this show() response to inner class only  #step 2
            print(self.cpu, self.brand, self.RAM)

s1 = Student("Michael", 2)
s2 = Student("ken", 3)

s1.show()  
#Michael 2
#Intel i5 HP Hynix DDR4 64GM RDIMM