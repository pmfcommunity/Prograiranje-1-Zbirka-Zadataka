# Korisnk unosi pozitivne cijele brojeve jedan ispod drugog. Kraj unosa korisnik oznacava sa -1. Program ispisuje
# sumu koju dobije tako sto sabira posljednje cifre za jednocifrene brojeve i predzadnje cifre za brojeve koji
# imaju vise od jedne cifre. 

suma = 0
while True: 
    n = int(input())
    if n == -1: break 
    if n > 0: 
        if n >= 10: 
            desetica = (n % 100) // 10
            suma += desetica
        else: suma += n 
print(suma)