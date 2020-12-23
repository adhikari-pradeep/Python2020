
class Students:

    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class... in abc module")


s1 = Students(36,67,32)
s2 = Students(89,32,72)

print(s1.avg())
print(s2.avg())

print(Students.getSchool())

Students.info()



