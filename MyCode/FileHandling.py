
f = open('MyData.txt', 'r')

# print(f.read())
# print(f.readline(), end='#')
# print(f.readline(), end='#')
# print(f.readline(), end='#')

# f1 = open('abc.txt', 'w')
# f1.write('Laptop')

# f2 = open('abc.txt', 'a')
# f2.write(' Mobile')

f2 = open('abc.txt', 'w')

# for data in f:
#     f2.write(data)

f3 = open('Capture.PNG', 'rb')

f4 = open('Pic.JPG', 'wb')

for i in f3:
    f4.write(i)
    print(i)