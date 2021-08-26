x = 0
y = 1
z = 1
endpoint = 5000
while z < endpoint:
    z = x+y
    x = y
    y = z
    if z < endpoint:
        print(z)