#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 

class computer: 
    pass 

c1 = computer()   #constructor  C1 or coupter() is constructor 
c2 = computer()  #constructor

print(id(c1))
print(id(c2))



##################################
class computer:
    def __init__(self):  #constructor   ?
        self.name = "micahel"   #define variable for the object 
        self.age = 28

c1 = computer()
c2 = computer()

c1.name = "kenneth"

print(c1.name)
print(c2.name)

=====
kenneth
michael