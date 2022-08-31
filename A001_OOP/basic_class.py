#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 

###understand the basic concept of special method __init__
##it is automacially run when the class is called 
#know how to define varible ...etc 

class computer:
    def conf(self):
        print('a+b')
        
    def conf2(self):
        print(3)

com1 = computer()
print(type(com1))
computer.conf(com1)  ##hey, computer , i want configruation for com1

computer.conf2(com1)

com1.conf() #this case you are use the object itself to call the function

'''
<class '__main__.computer'>
a+b
3
a+b

com1 is the object , parameter
'''