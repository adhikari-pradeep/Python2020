
class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell check")
        print("Convention Check")

class Laptop:

    def code(self,ide):
        ide.execute()

ide = MyEditor()


lap1 = Laptop()
lap1.code(ide)