# Napisati program koji narednim redoslijedom od korisnika uzima cetiri realne vrijednosti: alfa, n,k i h.
# Vrijednosti su unesene jedna ispod druge. Program ispisuje rezultat narednog izraza: 

from math import sin, cos, sqrt, radians 

alfa = float(input())
n = float(input())
k = float(input())
h = float(input())

alfa = radians(alfa)

rezultat = ((2 * k ** (2 / 3)) / (sin(alfa) * sqrt(h + n))) * cos(alfa)

print(rezultat)