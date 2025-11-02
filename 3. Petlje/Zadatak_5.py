# Korisnik unosi realne brojeve jedan ispod drugog. Kraj unosa oznacava praznim redom. Brojeve naizmjence uzimaju
# Harun i Sead. Prvi uneseni broj je Harunov, drugi Seadov, treci Harunov, cetvrti Seadov itd. Program ispisuje
# razliku sume Harunovih i sume Seadovih brojeva.

Harunova_suma = 0 
Seadova_suma = 0 
indeks = 1 

while True: 
    n = input()
    if n == "": break 
    else: 
        broj = float(n)
        if indeks % 2 != 0: 
            Harunova_suma += broj 
        if indeks % 2 == 0: 
            Seadova_suma += broj 
        indeks += 1
razlika = Harunova_suma - Seadova_suma
print(razlika)         