from functools import reduce


nums = [3,2,6,8,4,6,2,9]

eveNo = list(filter(lambda n : n%2==0 ,nums))

print(eveNo)

doubles = list(map(lambda n : n*2, eveNo))
print(doubles)

sum = reduce(lambda a,b : a+b, doubles)

print(sum)

def div(a,b):
    # if a<b:
    #     a,b = b,a
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)

div(2,4)