#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 
#understand baisc concept of __init__ 
#and how to define variable 
class computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram 

    def conf(self):
        print('The configuration is', self.cpu,self.ram)
    


com1 = computer('i5', 16)
com1.conf()