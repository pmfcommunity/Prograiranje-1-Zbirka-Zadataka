# Napisati program koji od korisnika trazi da unese petocifren broj. Program provjerava da li je uneseni broj
# petocifren, te ukoliko jeste, racuna i ispisuje razliku njegove najvece i najmanje cifre. Ukoliko broj nije 
# petocifren program ispisuje poruku: "Pogresan unos!"

petocifreni = int(input())

if petocifreni >= 10000 and petocifreni <= 99999:
    desetiljadarka = petocifreni // 10000
    hiljadarka = (petocifreni % 10000) // 1000
    stotica = (petocifreni % 1000) // 100
    desetica = (petocifreni % 100) // 10 
    jedinica = petocifreni % 10 
    
    najveca_cifra = max(desetiljadarka, hiljadarka, stotica, desetica, jedinica)
    najmanja_cifra = min(desetiljadarka, hiljadarka, stotica, desetica, jedinica)
    razlika = najveca_cifra - najmanja_cifra
    print(razlika)
else: print("Pogresan unos!")