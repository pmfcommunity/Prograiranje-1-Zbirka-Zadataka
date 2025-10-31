# Elipsoid je zatvorena centralno-simetricna ploha drugog reda. U sredistu elipsoida sijeku se tri medusobno
# okoite ose (glavne ose) simetrije. Elipsoid se moze parametarizirati na vise nacina, a najcesce koristen je:
# ... Napisati program koji od korisnika trazi parametre a, b, c, theta, phi, a program potom racuna i ispisuje
# vrijednosti koordinata x, y, i z.

from math import sin, cos, radians

a = float(input())
b = float(input())
c = float(input())
theta = float(input())
phi = float(input())

theta = radians(theta)
phi = radians(phi)

x = a * sin(theta) * cos(phi)
y = b * cos(theta) * sin(phi)
z = c * sin(theta)

print(x, y, z, sep='\n')