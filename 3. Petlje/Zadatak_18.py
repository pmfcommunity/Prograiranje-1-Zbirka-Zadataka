# Napisati program koji od korisnika zahtijeva unos cijelog broja n. Program ispisuje proizvod neparnih cifara
# tog broja koje su manje od 6. 

n = int(input())
proizvod = 1 

while n != 0: 
    cifra = n % 10 
    if cifra % 2 != 0 and cifra < 6: 
        proizvod *= cifra 
    n //= 10 
if proizvod == 1: proizvod = 0
print(proizvod)