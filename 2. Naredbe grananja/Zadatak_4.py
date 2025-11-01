# Napisati program koji od korisnika trazi da unese koordinate x i y cetra kruga, te poluprecnik kruga. Program
# zatim trazi unos dvije koordinate koje predstavlaju tacku A. Program provjerava da li unesena tacka A pripada
# unutrasnjosti kruga, da li se nalazi na kruznici ili se naalzi van kruznice, te na osnovu toga ispisuje 
# poruke: "Tacka pripada unutrasnjosti kruga", "Tacka pripada kruznici" ili "Tacka ne pripada krugu".

from math import sqrt 

epsilon = 0.000000000000001
x = float(input())
y = float(input())
r = float(input())
Ax = float(input())
Ay = float(input())

d = sqrt((Ax - x) ** 2 + (Ay - y) ** 2)

if d < r: print("Tacka pripada unutrasnjosti kruga")
elif d - r < epsilon and r - d < epsilon: print("Tacka pripada kruznici")
else: print("Tacka ne pripada krugu.")