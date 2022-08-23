###understand the basic concept of special method __init__
##it is automacially run when the class is called 


class computer:
    def __init__(self):
        print("in init")

    def conf(self):
        print('a+b')
    


com1 = computer()
com1.conf()

'''
in init
a+b
'''