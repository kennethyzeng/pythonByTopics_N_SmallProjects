#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 
#Question: When I remove @staticemethod above def info() and execute, it generate same result as static method. Why need to add "@static method" line then?

class Student: 

    school = 'modesto'   #class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3 

    def avg(self):     #instance method because it pass self(particular obj)
        return (self.m1 + self.m2 +self.m3)/3

    @classmethod
    def getSchoolName(cls):    #class method
        return cls.school 

    @staticmethod
    def info():
        print("this is student class  ...in abc module")

obj1 = Student(26, 36, 43)


#print(obj1.avg())
#print(Student.info())

Student.info()   #this is student class  ...in abc module