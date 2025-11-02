# Korisnik unosi pozitivne cijele brojeve jedan ispod drugog. Kraj unosa korisnik oznacava sa -1. Program 
# ispisuje sumu posljednjih cifara unesenih brojeva. 

suma = 0
while True: 
    n = int(input())
    if n == -1: break 
    if n > 0:
        jedinica = n % 10 
        suma += jedinica
print(suma)