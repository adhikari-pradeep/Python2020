

class Students:

    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'Lenevo'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Students("Adhikari", 7)
s2 = Students("Jenny", 3)

# print(s1.name, s1.rollNo)

s2.show()

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

