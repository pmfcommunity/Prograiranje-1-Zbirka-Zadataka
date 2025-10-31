# Ultrasonicni mjerac protoka mjeri brzinu tecnosti koristeci ultrazvuk da izmjeri volumen toka. Koristeci jedno
# vrijeme prolaska (tu), raspon izmedju izlaznog i ulaznog pretvaraca (L), ugla raspona (theta), i prosjecne
# tecnosti (Va) moguce je izracunati drugo vrijeme prolaska (td) koristeci formulu: ... Napisati program koji 
# od korisnika zahtijeva unos vrijednosti u redoslijedu Va, theta, L i tu, a ispisuje vrijeme prolaska td. 
# Takodjer, potrebno je uzeti u obzir da ce korisnik unijeti ugao u stepenima, a formula koristi radijane. 

from math import cos, radians 

Va = float(input())
theta = float(input())
L = float(input())
tu = float(input())

theta = radians(theta)

nazivnik = ((2 * Va * cos(theta)) / L) + (1 / tu)
td = 1 / nazivnik

print(td)