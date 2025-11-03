# Napisati program koji od korisnika uzima broj n. Program iscrtava pravougaonik dimenzija n redova i 
# 2n + 1 kolona, u formatu prikazanom u narednim primjerima.

n = int(input())

for i in range(n):
    for j in range(2 * n + 1):
        if i % 2 == 0 or j % 2 == 0: 
            print("x", end="")
        else: 
            print("0", end="")
    print()