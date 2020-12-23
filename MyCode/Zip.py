names = ("Navin", "Kiran", "Harsh")
comps = ("Dell", "Apple", "MS")

zipped = list(zip(names, comps)) #maintain order
zipped1 = set(zip(names, comps)) #dont maintain order
zipped2 = dict(zip(names, comps))

print(zipped)

for (a,b) in zipped:
    print(a,b)

