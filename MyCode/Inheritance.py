
class A:

    def features1(self):
        print("Features 1 is working")

    def features2(self):
        print("Features 2 is working")

class B:     #child class of A => class B(A)
    def features3(self):
        print("Features 3 is working")

    def features4(self):
        print("Features 4 is working")

class C(A,B):     #child class of A
    def features5(self):
        print("Features 5 is working")

    def features6(self):
        print("Features 6 is working")

a1 = A()

a1.features1()
a1.features1()

b1 = B()
b1.features3()
b1.features4()
# b1.features1()
# b1.features2()

c1 = C()
c1.features4()
c1.features2()
c1.features6()