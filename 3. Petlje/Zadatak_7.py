# Napisati program u koji korisnik unosi rijeci, svaku u zasebnoj linji. Korisnik oznacava kraj unosa praznim redom. 
# Program treba ispisati unesene rijeci odvojene praznim redom. 

recenica = ""
while True: 
    rijec = input()
    if rijec == "": break 
    recenica += rijec + " "    
print(recenica) 