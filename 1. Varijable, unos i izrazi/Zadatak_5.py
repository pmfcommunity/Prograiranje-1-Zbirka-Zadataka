# Napisati program koji kao ulaze podatke prima duzine dvije stranice trougla (b i c) i ugla izmedju njih
# (alfa). Program treba ispisati duzinu trece stranice a. 

from math import sqrt, cos, radians 

b = float(input())
c = float(input())
alfa = float(input())

alfa = radians(alfa)

a = sqrt(b ** 2 + c ** 2 - 2 * b * c * cos(alfa))

print(a)