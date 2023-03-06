import math
print ("введите число z:")
z = int(input())
print ("введите число c:")
c = int(input())
print ("введите число d:")
d = int(input())
print ("введите число k:")
k = int(input())

if z < 0:
    z**2-z
else:
    x = z**2-z
    y = math.pow(math.sin(c*x+d**2+k*x**2),3)
m = (min(x + y + z, x * y * z)) / (min(x - y + z, x * y / z))
print("ответ:", y)
print("ответ:", m)



