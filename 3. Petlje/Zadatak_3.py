# Korisnik unosi cijeli pozitivan broj n, a zatin n cijelih brojeva. Potrebno je kreirati trakasti grafikon 
# tako sto ce se za svaku unesenu vrijednost iscrtati toliko zvjezdica ili crtica u tom redu. Prva traka se 
# iscrtava crticama, drua zvjezdicama, treca opet crticama i tako naizmjenicno do samog kraja radi preglednosti.

n = int(input())
i = 1
lista_crtica_zvjezdica = []

while i <= n: 
    x = int(input())
    if i % 2 != 0: 
        lista_crtica_zvjezdica.append("-" * x)
    if i % 2 == 0:
        lista_crtica_zvjezdica.append("*" * x)
    i += 1
        
[print(lista) for lista in lista_crtica_zvjezdica]