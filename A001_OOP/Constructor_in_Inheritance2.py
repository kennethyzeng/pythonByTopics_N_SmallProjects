#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 
#see how the constructor response in inheritance 

class A: 
    def __init__(self):     #construtor for A
        print("in init A")

    def feature1(self):
        print("feature1 work okay")

    def feature2(self):
        print("feature2 work okay")

class B(A):     #inheritance
    def __init__(self):     #constructor for B
        print("in init B")

    def feature3(self):
        print("feature3 work okay")

    def feature4(self):
        print("feature4 work okay")


c = B()   #in init B #if you create a obj in B, first it find within its class; if not, it will call init of super class
d = A()   #in init A