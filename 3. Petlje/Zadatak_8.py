# Napisati program koji od korisnika zahtijeva unos cijelih brojeva, svaki u zasebnom redu. Korisnik oznacava
# kraj unosa praznm redom. Program ispisuje negirane vrijednosti u istom redu razdvojene praznim mjestom.

recenica = ""
while True: 
    unos = input()
    if unos == "": break 
    else: 
        broj = int(unos)
        recenica += str(-broj) + " "
print(recenica)