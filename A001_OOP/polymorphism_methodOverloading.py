#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 
#method overloading; double check with other lanague like java and c
#sum(a, b) 
#sume(a, b,c) or more parameter


class Student:

    def __init__(self, m1, m2):
        self.m1= m1
        self.m2 = m2 


    def sum(self, a=None,b=None, c=None):
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a +b 
        elif a != None: 
            s = a
        return s




s1 = Student(58,59)

print(s1.sum(6, 9))  #15
print(s1.sum(5))   #5
print(s1.sum(6,7, 5))  #18