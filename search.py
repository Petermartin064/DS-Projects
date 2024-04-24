def findElement(arr, n, value):
    for i in range(n):
        if arr[i] == value:
            return i

LA = [1, 2, 3, 4, 5]
print("The Element are\n")
for i in range(len(LA)):
    print("LA", i, "=", LA[i])
    
value = 4
n = len(LA)

index = findElement(LA, n, value)

if index != -1:
    print("Element", value, "Found at postion = ", str(index + 1))
else:
    print("Element not found")