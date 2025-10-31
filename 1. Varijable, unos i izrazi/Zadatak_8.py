# Pomocu vrijednosti izmjerenih prilikom kosog hica moguce je izracunati ubrzanje Zemljine teze g koristeci 
# formulu: ... gdje je V0 pocetko ubrzanje, R raspon, a alfa ugao izbacaja. Napisati program koji od korisnika
# zahtijeva unos vrijednosti u redoslijedu V0, R i alfa, a ispisuje ubrzanje Zemljine teze izracunato pomocu
# formule. Takodjer, potrebno je uzeti u obzir da ce korisnik unijeti ugao u stepenima, a formula koristi 
# radijane. 

from math import sin, radians 

V0 = float(input())
R = float(input())
alfa = float(input())

alfa = radians(alfa)

g = (V0 ** 2 / R) * sin(2 * alfa)

print(g) 