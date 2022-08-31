#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 
#Inner class 
#Example of create obj of inner class inside of the outer class 
#comparing with other inner class exmaple, why one is best to use? is it depdned on design situation?

class Student:   #outer class
    def __init__(self, name, rollno):
        self.name = name 
        self.rollno = rollno 
        self.lap = self.Laptop()  #step 2. create obj outside of inner class

    def show(self): 
        print(self.name, self.rollno)    


    class Laptop:     #step 1   inner class
        def __init__(self):
            self.brand = "HP"
            self.cpu = "Intel i5"
            self.RAM = "Hynix DDR4 64GM RDIMM"

s1 = Student("Michael", 2)
s2 = Student("ken", 3)

s1.show()   #print(s1.name, s1.rollno) , same reult

lap1 = s1.lap
lap2 = s2.lap


print(lap1)       #<__main__.Student.Laptop object at 0x10541b310>
print(id(lap1))    #4383159056
print(lap1.brand)   #HP