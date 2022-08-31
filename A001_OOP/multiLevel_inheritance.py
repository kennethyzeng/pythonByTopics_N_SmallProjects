#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 
'''
class A:
      feature1 and feature2 

class B:
      feature1 and feature2
      feature3 and feature4
class C: 
    feature1 and feature2
    feature3 and feature4
    feature5 and feature6
'''

class A: 
    def feature1(self):
        print("feature1 work okay")

    def feature2(self):
        print("feature2 work okay")

class B(A):     #inheritance from A
    def feature3(self):
        print("feature3 work okay")

    def feature4(self):
        print("feature4 work okay")

class C(B): #inheritance from B
    def feature5(self):
        print("feature5 work okay")

    def feature6(self):
        print("feature6 work okay")

d = C()
d.feature1()   #feature1 work okay
d.feature3()   #feature3 work okay
d.feature5()   #feature5 work okay