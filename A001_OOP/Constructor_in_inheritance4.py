#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 
##see how the constructor response in inheritance 
'''
class A:
      feature1 and feature2 

class B:
      feature3 and feature4
class C: 
    feature1 and feature2
    feature3 and feature4
    feature5 and feature6
'''

class A: 
    def __init__(self):     #construtor for A
        print("in init A")

    def feature1(self):
        print("feature 1-A work okay")     #see here

    def feature2(self):
        print("feature2 work okay")

class B:
    def __init__(self):     #construtor for A
        print("in init B")

    def feature1(self):   
        print("feature 1-B work okay")    #see here

    def feature4(self):
        print("feature4 work okay")

class C(A, B): #inheritance from A and B

    def __init__(self):     #construtor for C
        super().__init__()
        print("in init C")

    def feature5(self):
        print("feature5 work okay")

    def feature6(self):
        print("feature6 work okay")
        
    def feat(self):
        super().feature2()

###what will be the output?
d = C()

#in init A
#in init C
#why? Mehtod Resolution Order(MRO)  left to right? mean 1st to 2nd ?

d.feature1()  #feature 1-A work okay
#why From A class. still Mehtod Resolution Order(MRO)

d.feat()   #feature2 work okay