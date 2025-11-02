# Napisati program koji od korisnika zahtijeva unos cijelih brojeva, svaki u zasebnom redu. Korisnik oznacava
# kraj unosa praznim redom. Proram ispisuje "Nalazi se!" ukoliko se broj 2 nalazi medu unesenim vrijednostima.
# Program ispisuje "Ne nalazi se!" ukoliko se broj 2 ne nalazi medu unesenim vrijednostima.

jel_dvica = False 
while True: 
    n = input()
    if n == "": break 
    if int(n) == 2: jel_dvica = True 
if jel_dvica: print("Nalazi se!")
else: print("Ne nalazi se!")