# Funkcija f definise se po segmentima sa ... Napisati program koji ce za datu vrijednost promjenjive x 
# izracunati vrijednost funkcije f(x).

x = int(input())

funkcija = 0 

if x <= -2: funkcija = -1 
elif 0 < x <= 100: funkcija = 1 / (3 + 2 / x)
elif x >= 105: funkcija = 200 
else: funkcija = 0

print(funkcija)