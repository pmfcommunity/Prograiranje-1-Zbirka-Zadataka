# Napisati program koji od korisnika trazi da unese ostvarene bodove iz predmeta Programiranje. Korisnik unosi 
# broj osvojenih bodova na vjezbama, broj osvojenih bodova na parcijalnim ispitima, kao i na zavrsnom. 
# Program korisniku ispisuje konacnu ocjenu. Koristi se zakonska skala za ocjenjivanje: 95-100 je ocjena 10, 
# 85-94 je ocjena 9, 75-84 je ocjena 8, 65-74 je ocjena 7, 55-64 je ocjena 6. U slucaju ostvarenog manjeg broja
# bodova, student nije polozio predmet, te upisuje ocjenu 5. 

bodovi_sa_vjezbi = int(input("Unesite broj bodova na vjezbama: "))
bodovi_sa_parcijalnih = int(input("Unesite broj bodova sa parcijalnih ispita: "))
bodovi_sa_zavrsog = int(input("Unesite broj bodova sa zavrsnog ispita: "))

if bodovi_sa_vjezbi < 0 or bodovi_sa_vjezbi > 20 or \
    bodovi_sa_parcijalnih < 0 or bodovi_sa_parcijalnih > 40 or \
        bodovi_sa_zavrsog < 0 or bodovi_sa_zavrsog > 40:
            print("Pogresan unos bodova!")
            print(f"Broj bodova sa vjezbi: {bodovi_sa_vjezbi} (0-20)")
            print(f"Broj bodova sa parcijalnih: {bodovi_sa_parcijalnih} (0-40)")
            print(f"Broj bodova sa zavrsnog: {bodovi_sa_zavrsog} (0-40)")
else: 
    ukupan_broj_bodova = bodovi_sa_vjezbi + bodovi_sa_parcijalnih + bodovi_sa_zavrsog
    
    ocjena = 0
    if ukupan_broj_bodova >= 95: ocjena = 10
    elif ukupan_broj_bodova >= 85: ocjena = 9
    elif ukupan_broj_bodova >= 75: ocjena = 8
    elif ukupan_broj_bodova >= 65: ocjena = 7
    elif ukupan_broj_bodova >= 55: ocjena = 6
    else: ocjena = 5
    print(f"Ukupan broj bodova za predmet: {ukupan_broj_bodova}\nOcjena: {ocjena}")