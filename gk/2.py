b = input().split()
c = set()

for x in b:
    for y in x:
        c.add(y)
print(list(c))
