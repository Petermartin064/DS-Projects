LA = [0, 0, 0]
n = len(LA)

print("Array before deletion\n")
for x in range(n):
    print("Array", x, "=", LA[x])

#Deleting Element
for x in range(len(LA)):
    LA.append(x)
    LA[x] = x+3
    print("LA", x, "=", LA[x])

for x in range(1, n-1):
    LA[x] = LA[x+1]
    n -= 1

print("\nArray after deletion")
for x in range(n):
    print("Array", x, "=", LA[x])