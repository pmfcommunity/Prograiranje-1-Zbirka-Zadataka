# U geometriji, upisana kruznica trougla je najveca kruznica koju sadri trougao. Kruznica dodiruje sve tri 
# stranice trougla. Poluprecnik kruznice r se izrazava kao ... Napisati program koji od korisnika trazi unos
# uglova alfa i beta, te duzinu stranice c trougla, a potom racuna i ispisuje vrijednost poluprecnika r upisane
# kruznice.

from math import sin, cos, radians

alfa = float(input())
beta = float(input())
c = float(input())

gamma = 180 - alfa - beta 

alfa = radians(alfa)
beta = radians(beta)
gamma = radians(gamma)

r = c * ((sin(alfa / 2) * sin(beta / 2)) / cos(gamma / 2))

print(r)