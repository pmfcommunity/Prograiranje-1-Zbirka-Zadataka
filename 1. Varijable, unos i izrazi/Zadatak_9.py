# Prilikom simulacije kosog hica potrebno je izracunati pocetnu brzinu objekta. Ukoliko je data trenutna 
# pozicija objekta (x, y) i ugao izbacaja alfa, pocetna brzina se racna koristeci formulu: ... gdje je g 
# ubrzanje Zemljine teze i ima vrijednost 9.81. Napisati program koji od korisnika zahtijeva unos vrijednosti
# u redoslijedu x, y, i alfa, a ispisuje pocetnu brzinu izracunatu pomocu formule. Takodjer, potrebno je uzeti
# u obzir da ce korisnik unijeti ugao u stepenima, a formula koristi radijane. 

from math import sqrt, sin, cos, radians 

x = float(input())
y = float(input())
alfa = float(input())

G = 9.81
alfa = radians(alfa)

V0 = sqrt((x ** 2 * G) / (x * sin(2 * alfa) - 2 * y * cos(alfa) ** 2))

print(V0)