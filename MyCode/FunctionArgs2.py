
def person(name, **data):

    # print(name)
    # print(data)

    for i,j in data.items():
        print(i,j)

#keyword variable argument
person('adhikari', age=30, city='Texas',zip=76040)
