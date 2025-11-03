# Korisnik unosi pozitivan cijeli broj n. Program ipsisuje duzinu najduzeg raspona u kojem su sve uzastopne 
# cifre vece od 4.

n = int(input())

lista_n = list(str(n))
recenica = ""
lista_raspona = []

for lista in lista_n:
    broj = int(lista)
    if broj > 4:
        recenica += str(broj)
    if broj < 4:
        lista_raspona.append(recenica)
        recenica = ""
najveci_raspon = max(lista_raspona)
print(len(najveci_raspon))

# 928632978158