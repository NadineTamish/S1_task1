amount = int(input())

pounds = [200, 100, 50, 20, 10, 5, 1]
result = ""

for i in pounds:
    count = amount // i
    if count > 0:
       result+=count X i L.E.+ 
       amount -= count * i

result = result.rstrip(" + ")
print(result)