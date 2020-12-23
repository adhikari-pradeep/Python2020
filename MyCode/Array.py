import array as arr
#array needs same type value


vals = arr.array('i', [5, 9, 8, 4, 2])
# vals.reverse()

# for i in range (len(vals)):
#     print(vals[i])

newArr = arr.array(vals.typecode, (a*a for a in vals))

for e in vals:
    print(e)

print('-----------')

for e in newArr:
    print(e)

print('-----------')

i=0

while i<len(newArr):
    print(newArr[i])
    i+=1

print('-----------')

val = arr.array('u',['a','e','i','o','u'])

for e in val:
    print(e)

"""
this is use for documentation
"""
# use for comments