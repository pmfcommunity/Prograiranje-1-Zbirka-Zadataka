# Napisati program koji ispisuje sve trocifrene brojeve koji ispunjavaju uslov: 
# abc = a^3 + b^3 + c^3 
# gdje a, b i c predstavljaju cifre trocifrenog broja. Program ispisuje brojeve od najmanjeg ka najvecem u 
# istom redu, ali razdvojene praznim mjestom. 

# I. nacin (iz zbirke)

for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            broj = a * 100 + b * 10 + c 
            if broj == a ** 3 + b ** 3 + c ** 3:
                print(broj, end=" ")
print('\n')

# II. Nacin (laksi)

i = 100 
while i <= 999: 
    a = i // 100
    b = (i % 100) // 10
    c = i % 10 
    if i == a ** 3 + b ** 3 + c ** 3:
        print(i, end=" ")
    i += 1