##understand theory of self. 
##When calling method, self is port to c1 object 
##when multiple objects(like c1, c2, c3, etc) are creates, self is point to its own object. 
##different object has different memory location(head memory)=> you can check with id() 

class computer:
    def __init__(self):
        self.name = "micahel"
        self.age = 28

    def update(self):
        self.age = 30

c1 = computer()
c2 = computer()

c1.name = "kenneth"
c1.age =12 
c1.update()     #when calling method, self is point to c1 object

#print(c1.name)
#print(c2.name)
print(c1.age)      ##30