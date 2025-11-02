# Korisnik prvo unosi cijeli pozitivan broj n, a zatim n rijeci jednu ispod druge. Program treba ispisati 
# "jeste" ukoliko je korisnik upisao rijec "programiranje" tacno dva puta, a u svakom drugom slucaju program
# ispisuje "nije". 

n = int(input())

i = 0 
brojac = 0
while i < n: 
    rijec = input()
    if rijec.lower() == "programiranje": brojac += 1 
    i += 1 
if brojac == 2: print("jeste")
else: print("nije")