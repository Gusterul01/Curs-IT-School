'''Problema 1. Se citeste de la tastatura o parola. Sa se verifice daca parola introdusa are
    cel putin 10 caractere si nu contine spatiu.
Sa se afiseze un mesaj corespunzator pentru fiecare neregula gasita
    sau mesajul "OK" in cazul in care parola respecta regulile.
    hints: boolean, conditionals'''

# PRIMA PROBLEMA

'''

i = 0

while True:
    try:
        parola = input("Introduce o parola. Parola trebuie sa aiba cel putin 10 caractere si sa nu contina spatiu:")

        if (len(parola) >= 10) and (parola[i] != ' '):
            i += 1
            break

        elif (parola[i] == ' '):
            print("Parola introdusa contine spatii.")
            i -= 1

        elif (len(parola) < 10):
            print("Parola introdusa are mai putin de 10 caractere.")
            i -= 1
    except:
        print("Parola invalida")

print("OK")
'''

'''Problema 2. Sa se numere de cate ori apare o litera intr-un cuvant.'''

# A 2-A PROBLEMA

'''i=0
aparitii = 0

cuvant = input("Scrie un cuvant: ")

for i in cuvant:
    if i == "a":
        aparitii += 1

print(f"Cuvantul {cuvant} contine {aparitii} 'a'")'''



'''Problema 3. Sa se afiseze toate toate puterile lui 3 cuprinse intre 200 si 300.'''

# PROBLEMA A 3-A
'''
i = 0


for i in range(0, 20):
    putere = 3 ** i
    if 200 <= putere <= 300:
        print(f"Puterea lui 3 din intervalul 200 - 300 este {putere}")
        i += 1

'''




'''Problema 4. Se citeste un numar de la tastatura. 
    Sa se calculeze suma numerelor de la 1 pana la numarul citit. (folositi for si while)'''

#PROBLEMA A 4-A
'''
numar = int(input("Alege un numar: "))
suma = 0
i = 1

for i in range(1, numar + 1):
    suma += i
    i += 1
print(suma)
numar = int(input("Alege un numar"))
i = 1
suma = 0

while True:
    if i == numar + 1:
        break
    i += 1
    print(suma)
    suma = ((i * (i + 1)) / 2)
'''

'''Problema 5. Rezolvati folosind doua variante: Varianta 1 -> FOR
                                                Varianta 2 -> WHILE
   Se citeste un numar n de la tastatura. Sa se scrie un program care
    face o numaratoare inversa de la numarul respectiv pana la 0.'''

# PROBLEMA A 5-A
'''
n = int(input("Alege un numar: "))

for i in range(n, -1, -1):
    print(i)



n = int(input("Alege un numar: "))

i = -1

while n >= 0:
    print(n)
    n -= 1

'''
'''Problema 6. Rezolvati folosind doua variante: Varianta 1 -> FOR
                                                Varianta 2 -> WHILE
    Se citeste un numar de la tastatura. Sa se calculeze 
        suma numerelor de la 1 pana la numarul citit. (folositi for si while)'''

# --------------------------------- #