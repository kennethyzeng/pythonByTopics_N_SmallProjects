class Student:

    def __init__(self, m1, m2):
        self.m1= m1
        self.m2 = m2 

    def __add__(self, other):   #operator overloading
        m1 = self.m1 + other.m1 
        m2 = self.m2 + other.m2
        return Student(m1, m2)    #
        #print(m1)   #121

    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2   #
        if r1 > r2:
            return True 
        else:
            return False 

    def __str__(self):
        return self.m1, self.m2     #(num1, num2)
        #return '{} {}'.format(self.m1, self.m2)      #num1, num2
    


s1 = Student(44, 56)
s2 = Student(77 , 88)
  
ans = s1 + s2    ##without re-define __add__, fail to use +
#print(ans)    without overriding __str__, it will show <__main__.Student object at 0x10deeda80>
print(ans.__str__())   #(121, 144)     
print(ans.m1)  #121


#####
if s1 > s2 :
    print("s1 win")
else: 
    print("s2 win")

###

print(s1.__str__())   #(44, 56)
