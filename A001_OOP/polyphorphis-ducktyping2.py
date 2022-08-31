#polythorphism : duck-typing
class Pycharm: 
    def execute(self):
        print("compliling")
        print("running")


class MyEditor:
    def execute(self):
        print("Sepll Check")
        print("Convention Check")
        print("compling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()

#ide = Pycharm()
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

#Sepll Check
#Convention Check
#compliling
#running

