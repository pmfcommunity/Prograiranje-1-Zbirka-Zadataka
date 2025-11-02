# Napisati program u koji korisnik unosi pozitivne brojeve, svaki u zasebnoj liniji. Korsinik oznacava kraj unosa
# brojem -1. Ukoliko je uneseni broj paran program ispisuje njegovu negiranu vrijednost, a ako nije, program
# ispisuje broj u originalnom obliku. 

while True: 
    n = int(input())
    if n == -1: break
    if n % 2 == 0:
        print(-n)
    else: print(n)