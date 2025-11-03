# Napisati program koji od korisnika zahtijeva unos cijelog broja. Program provjerava da li su cifre unesenog
# broja sa lijeva na desno u monotono opadajucem redoslijedu. Drugim rijecma, program provjerava da li vrijedi
# da je an >= an + 1, gdje a predstavlja jednu cifru broja, a n njegovu poziciju. 
# Ukoliko su cifre unesenog broja u monotono opadajucem redoslijedu program ispisuje "jesu", a u suprotnom
# program ispisuje "nisu"

n = int(input())
jel_monoton = True 

if n < 10: 
    jel_monoton = False 
else: 
    while n // 10 != 0: 
        cifra_1 = n % 10 
        cifra_2 = (n % 100) // 10
        if cifra_1 > cifra_2:
            jel_monoton = False 
            break
        else: n //= 10 
if jel_monoton: print("jesu")
else: print("nisu")