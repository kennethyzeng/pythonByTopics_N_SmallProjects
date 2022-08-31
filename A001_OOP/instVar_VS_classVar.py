#Created by kenneth Zeng 
#the purpos of these code is for quick study for prepaing interview or catch up for job or refresh memory. sometime, easy code is fast to catch up 

##understand instance variable VS. class variable 
# class Variable is similar to global variable 
# if you change value of class vaiable, it impact the value of that particular variable for each object  
class Car: 
    wheels = 4 
    #wheels is class Variable 

    def __init__(self):
        self.mil = 10
        self.mod = "BMW"
        #mil and mod is instance variables

c1 = Car() 
c2 = Car() 

c1.mil = 0 
Car.wheels = 5

print(c1.mod, c1.mil, c1.wheels)
print(c2.mod, c2.mil, c2.wheels)


##output:
# BMW 0 5
#BMW 10 5