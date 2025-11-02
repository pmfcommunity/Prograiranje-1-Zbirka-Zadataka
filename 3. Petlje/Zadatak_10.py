# Korisnik unosi visecifren prirodan broj. Program ispisuje razliku proizvoda i kolicnika najvece i najmanje 
# cifre broja. Moze se pretpostaviti da niti jedna cifra nema vrijednost 0. 

n = int(input())
lista_cifara_broja = []

while n != 0: 
    jedinica = n % 10 
    lista_cifara_broja.append(jedinica)
    n //= 10 
najveca_cifra = max(lista_cifara_broja)
najmana_cifra = min(lista_cifara_broja)

proizvod = najveca_cifra * najmana_cifra 
kolicnik = najveca_cifra / najmana_cifra 
razlika = proizvod - kolicnik 

print(razlika)