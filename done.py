

listen = ["banana", "Orange", "Kiwi", "cherry"]

print(listen)
print(len(listen))

print()

x = 0
y = 1
while x <= len(listen):
    z = 0
    while z < y:
        z += 1
        print('\t')
        
    print(listen[x] + '\n')
    x += 1
    y += 1