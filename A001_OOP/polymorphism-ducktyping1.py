class Pycharm: 
    def execute(self):
        print("compliling")
        print("running")



class Laptop:
    def code(self, ide):
        ide.execute()

ide = Pycharm()


lap1 = Laptop()
lap1.code(ide)

#compliling
#running