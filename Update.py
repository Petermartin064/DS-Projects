LA = [0, 1, 2,]

print("The Original Array")
for i in range(len(LA)):
    print("LA", i, "=", LA[i])

print("Updated Array")

LA[2] = 4

for i in range(len(LA)):
    print("LA", i, "=", LA[i])