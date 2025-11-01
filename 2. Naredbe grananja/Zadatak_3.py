# Napisati program koji od korisnika trazi da unese trocifren broj. Program provjerava da li je uneseni broj
# trocifren, te ukoliko jeste, racuna i ispisuje proizvod njegovih cifara. Ukoliko nije trocifren program
# ispisuje poruku: "Pogresan unos!"

n = int(input())

if n >= 100 and n <= 999:
    stotica = n // 100
    desetica = (n % 100) // 10
    jedinica = n % 10 
    proizvod = stotica * desetica * jedinica
    
    print(proizvod) 
else: print("Pogresan unos!")