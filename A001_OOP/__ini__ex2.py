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