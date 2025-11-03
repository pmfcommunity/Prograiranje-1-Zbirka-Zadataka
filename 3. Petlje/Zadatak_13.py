# Za prirodan boj kazemo da je fin ako sadrzi dvije uzastopne cifre cija je suma 4. Korisnik unosi prirodan broj 
# n. Program ispisuje n-ti fin prirodan broj.

n = int(input())
suma = 0
ispis = str(n)

if n >= 10:
    kopija = n 
    while kopija != 0:
        cifra = kopija % 10
        suma += cifra 
        kopija //= 10
indeks = 1 
jel_fin_broj = False 
while True: 
    if n >= 10: 
        fin_broj = suma + indeks 
        if fin_broj == 4: 
            ispis += str(indeks)
            break 
    else: 
        fin_broj = n + indeks 
        if fin_broj == 4:
            ispis += str(indeks)
            break 
    indeks += 1
print(ispis)