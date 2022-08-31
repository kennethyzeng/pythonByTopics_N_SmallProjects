#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 
#instance method inlcude accessor method and mutator method. do you see the different . one is get value another one is set value.    (self) and (self, value)

class Student: 
    school = 'modesto'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3 

    def avg(self):     #instance method because it pass self(particular obj)
        return (self.m1 + self.m2 +self.m3)/3

    def get_m1(self):   #accessor method
        return self.m1
    
    def set_m1(self, value):    ##mutator method
        self.m1 = value 

obj1 = Student(26, 36, 43)
print(obj1.avg())


obj1.set_m1(99)
obj1.get_m1()
print(obj1.avg())

######output 
# 35.0
#59.333333333333336

