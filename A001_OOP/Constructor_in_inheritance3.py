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
        super().__init__()
        super().feature1()
        print("in init B")
        #super().__init__()

    def feature3(self):
        print("feature3 work okay")

    def feature4(self):
        print("feature4 work okay")


c = B()   
#in init A
#feature1 work okay
#in init B

#note: if #super().__init__() below print("in init B")
#output: in init B  then in init A