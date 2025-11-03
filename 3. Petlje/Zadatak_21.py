# Za neki broj n kazemo da je savrsen ukoliko je jednak sumi svih svojih pozitivnih djelilaca manjih od n. 
# Na primjer, 28 je savrsen broj: njegovi djelioci su 1, 2, 4, 7, i 14, a 1 + 2 + 4 + 7 + 14 = 28. Napisati
# program koji trazi unos cijelih brojeva a i b, a koji zatim ispisuje sve savrsene brojeve u opsegu od a do b,
# jedan ispod drugog. 

a = int(input())
b = int(input())

indeks = a  
while indeks <= b:
    suma = 0  
    for i in range (1, indeks): 
        if indeks % i == 0: 
            suma += i 
    if suma == indeks: 
        print(indeks)
    indeks += 1