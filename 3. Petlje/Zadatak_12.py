# Korisnik unosi dva pozitivna cijela broja a i b. Program ispisuje sve brojeve u rasponu od a do b (ukljucujuci)
# obje rijednosti) koji su djeljivi sa 3 ili koji u sebi sadrze barem jednu cifru djeljivu sa 3. Brojevi se
# ispisuju od najmanjeg ka najvecem u istom redu razdvjeni jednim praznim mjestom. [Napomena: 0 je djeljiva 
# sa 3.]

a = int(input())
b = int(input())

indeks = a
lista_cifara = [] 
while indeks <= b: 
    if indeks % 3 == 0:
        lista_cifara.append(indeks)
    if indeks % 3 != 0:
        kopija = indeks 
        while kopija != 0:
            cifra = kopija % 10 
            if cifra % 3 == 0 or cifra == 0: 
                lista_cifara.append(indeks)
            kopija //= 10 
    indeks += 1
[print(cifra, end=" ") for cifra in lista_cifara]