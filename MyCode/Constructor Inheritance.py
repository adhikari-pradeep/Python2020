
class A:
    def __init__(self):
        print("in A Init")

    def features1(self):
        print("Features 1 is working")

    def features2(self):
        print("Features 2 is working")

class B:     #child class of A => class B(A)
    def __init__(self):
        # super().__init__()
        print("in B Init")


    def features3(self):
        print("Features 3 is working")

    def features4(self):
        print("Features 4 is working")


class C(B,A):   #MRO from Left to Right

    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().features2()


a1 = C()

