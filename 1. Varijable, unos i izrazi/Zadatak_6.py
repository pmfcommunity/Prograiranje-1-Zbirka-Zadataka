# Napisati program koji izracunava zapreminu torusa: ... gdje je R udaljenost od centra cijevi do sredista torusa,
# a r je oluprecnik cijevi. Program od korisnika trazi unos ove dvije vrijednosti, a ispisuje zapreminu. Za 
# vrijednost pi potrebno je koristiti konstantu pi iz biblioteke math.

from math import pi 

R = float(input())
r = float(input())

V = 2 * pi ** 2 * R * r ** 2 

print(V)