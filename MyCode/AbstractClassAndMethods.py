# abstract class
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")


class Programmer():
    def work(self,com):
        print("Solving Bugs")
        com.process()

# com = Computer()
# com.process()

com1 = Laptop()
# com1.process()


prog1 = Programmer()
prog1.work(com1)