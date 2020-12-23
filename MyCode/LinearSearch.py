
pos = -1 #local variable

def search(list, n):
    i = 0

    while i< len(list):
        if list[i] == n:
            globals() [ 'pos' ] = i #pos is local variable
            return True
        i = i + 1

    return False

list = [5,8,4,6,9,2]
n = 9

if search(list,n):
    print("Found at ", pos, " position")
else:
    print("Not Found")