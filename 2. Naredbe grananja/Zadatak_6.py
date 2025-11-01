# Napisati program koji od korisnika trazi da unese x i y koordinate centara za dva kruga u dvodimenzionalnoj 
# ravni. Koordinate se unose jedna ispod druge. Korisnik unosi i duzinu poluprecnika prvog kruga. Poluprecnik
# prvog kruga jednak je precniku drugog kruga. Provjeriti da li se uneseni krugovi sijeku, te shodno ispisati
# jednu od naredne tri poruke: "Kruznice se sijeku", "Kruznice se dodiruju" ili "Kruznice nemaju zajednickih
# tacaka".

from math import sqrt 

epsilon = 0.000000000000001
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
r1 = float(input())

r2 = r1 / 2
d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

Rzbir = r1 + r2 
Rrazlika = abs(r1 - r2)

if Rrazlika < d < Rzbir: print("Kruznice se sijeku.")
elif abs(d - Rrazlika) < epsilon or abs(d - Rzbir) < epsilon: print("Kruznice se dodiruju")
else: print("Kruznice nemaju zajednickih tacaka.")