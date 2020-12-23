
def update(x):


    x=8
    print(x)

a=10
update(a)

def person(name, age=18):
    print(name)
    print(age)

person(age=30, name='Adhikari')

person(name='Adhikari')

print("-------------------")

def sum(x, *y):

    c=x

    for i in y:
        c=c+i
    print(c)

sum(5,7,11,6)