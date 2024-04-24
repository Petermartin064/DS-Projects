array = [0, 0, 0]
x = 0
print("Array before insertion")
for x in range(len(array)):
    print("Array", x, "==", array[x])
    
#Inserting Element
for x in range(len(array)):
    array.append(x)
    array[x] = x+1
    
print("Array after insertion")
for x in range(len(array)):
    print("Array", x, "==", array[x])
