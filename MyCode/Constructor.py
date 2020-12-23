

class Computer:

    def __init__(self):
        self.name = "Adhikari"
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 20
c2 = Computer()

if c1.compare(c2):
    print("They are same age")
else:
    print("They are different age")

print(c1.name)
print(c2.name)