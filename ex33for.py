i = 0
numbers= []
for i in range(0,6):
     print(f"At the top i is: {i}")
     numbers.append(i)

     i = i + 1
     print("Numbers now: ",numbers)
     print(f"At the bottom i is {i}")
print("The numbers: ")

for num in numbers :
    print(num)
