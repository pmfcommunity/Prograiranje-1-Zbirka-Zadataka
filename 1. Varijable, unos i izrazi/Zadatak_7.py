# Kartezijeve koordinate x i y se mogu pretvoriti u polarne koordinate r i phi koristeci: ... Napisati program
# koji od korisnika trazi unos vrijednosti za x i y, a ispisuje r i phi na zasebnim linijama. Za izracun 
# funkcije arctan mozete koristiti Pythonovu funkciju math.atan2(y, z) koja prima dva parametra (brojnik i 
# nazivnik) umjesto razlomka. Takodjer, ugao phi je potrebno ispisati u stepenima a ne u radijanima za sta
# mozete koristiti funkciju math.degrees()

from math import sqrt, atan2, degrees

x = float(input())
y = float(input())

r = sqrt(x ** 2 + y ** 2)

phi = atan2(y, x)
phi = degrees(phi)

print(r, phi, sep="\n")