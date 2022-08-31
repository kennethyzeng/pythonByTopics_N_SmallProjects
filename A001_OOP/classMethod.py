#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 



class Student: 
    school = 'modesto'   #class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3 

    def avg(self):     #instance method because it pass self(particular obj)
        return (self.m1 + self.m2 +self.m3)/3

    @classmethod     #have add this one 
    def getSchoolName(cls):
        return cls.school 
    

obj1 = Student(26, 36, 43)


#print(obj1.avg())
print(Student.getSchoolName())   #getSchoolName() not getSchoolName(cls)

##output: modesto