'''Problema 1. Operatii aritmetice
Scrie un program care:
    - Cere doua numere si calculeaza:
        - Suma
        - Diferenta
        - Produsul
        - Impartirea
        - Imaprtirea intreaga
        - Restul impartirii (modulo)
        - Puterea
    - La final, afiseaza fiecare rezultat
'''

#Incepe de aici problema 1


print(F"PRIMA PROBLEMA: ")

numarul1 = float(input(f"Introduce primul numar: "))

numarul2 = float(input(f"Introduce al 2-lea numar: "))

suma = numarul1 + numarul2

diferenta = numarul1 - numarul2

produsul = numarul1 * numarul2

impartirea = numarul1 / numarul2

impartirea_int = numarul1 // numarul2

restul = numarul1 % numarul2

sqrt = numarul1 ** numarul2

print(f"REZULTATE: ")
print(f"Suma celor doua numere este: {suma}" )
print(f"Diferenta celor doua numere este: {diferenta}" )
print(f"Produsul celor doua numere este: {produsul}" )
print(f"Impartirea celor doua numere este: {impartirea}" )
print(f"Impartirea intreaga a celor doua numere este: {impartirea_int}" )
print(f"Restul impartirii celor doua numere este: {restul}" )
print(f"Puterea celor doua numere este este: {sqrt}" )

#Sfarsit problema 1


'''Problema 2. Tipuri de date
Declara cate o variabila pentru fiecare tip de date studiat si afiseaza tipul acesteia
'''

#Incepe de aici problema 2
""""""
print(F"A 2-A PROBLEMA: ")

nume = "Andrei"

numar_intreg = 3

numar_float = 3.4

numar_complex = 3j

adevar = True

print(type(nume))
print(type(numar_intreg))
print(type(numar_float))
print(type(numar_complex))
print(type(adevar))
""""""

#Sfarsit problema 2


''' Problema 3. Transforma din minute in ore si minute
    - Primeste de la tastatura un numar de minute(ex. 135)
    - Afiseaza cate ore si minute reprezinta acel numar
'''

#Incepe de aici problema 3
print(F"A 3-A PROBLEMA: ")

minute = int(input(f"Durata in minute este: "))

ore = minute // 60
rest = minute % 60

print(f"Durata este de: {ore} ore si {rest} minute")


#Sfarsit problema 3


''' Problema 4. Bonul de cumparaturi
O persoana cumpara 3 produse. Vrem sa afisam:
    - Totalul fara TVA
    - TVA(ex. 19%)
    - Totalul cu TVA
'''

#Incepe de aici problema 4

print(f"A 4-A PROBLEMA: ")

Produsul1 = int(input(f"Introdu pretul primului produs: "))
Produsul2 = int(input(f"Introdu pretul celui de-al 2-lea produs: "))
Produsul3 = int(input(f"Introdu pretul celui de-al 3-lea produs: "))

TVA1 = Produsul1 * 19 / 100
TVA2 = Produsul2 * 19 / 100
TVA3 = Produsul3 * 19 / 100

Total_fara = (Produsul1 + Produsul2 + Produsul3) - (TVA1 + TVA2 + TVA3)
Total_cu_tva = Produsul1 + TVA1 + Produsul2 +TVA2 + Produsul3 + TVA3

print(f"Totalul fara TVA al produselor este: {Total_fara}")
print(f"TVA-ul primului produs este: {TVA1}")
print(f"TVA-ul celui de-al 2-lea produs este: {TVA2}")
print(f"TVA-ul celui de-al 3-lea produs este: {TVA3}")
print(f"Totalul cu TVA al produselor este: {Total_cu_tva}")


#Sfarsit problema 4

'''Problema 5. Bugetul pentru un concediu
Cerinta: Un grup de prieteni planuieste o vacanta. Trebuie sa calculezi: 
    - Contributia totala
    - Costul cheltuielilor (transport, cazare, mancare pe zile)
    - Ce suma ramane pentru distractii

Date de intrare: 
    - Numarul de prieteni
    - Suma de bani per persoana
    - Costul transportului
    - Costul pe zi pentru cazare
    - Costul pe zi pentru mancare
    - Numarul de zile
'''

#Incepe de aici problema 5

print(f"A 5-A PROBLEMA: ")

prieteni = int(input(f"Introdu numarul de persoane: "))
bani_persoana = float(input(f"Introdu numarul de bani pe care-l plateste fiecare persoana: "))
transport = float(input(f"Introdu costul transportului: "))
cost_cazare = float(input(f"Introdu costul fiecarei zi de cazare: "))
cost_mancare = float(input(f"Introdu costul mancarii pentru fiecare zi: "))
zile = int(input(f"Introdu numarul de zile al concediului: "))

suma_stransa = prieteni * bani_persoana
cost_cheltuieli = transport + (cost_mancare * zile) + (cost_cazare * zile)
suma_distractii = suma_stransa - cost_cheltuieli

print(f"Suma de bani stransa este: {suma_stransa}")
print(f"Costul total al cheltuielilor este: {cost_cheltuieli}")
print(f"Suma de bani ramasa pentru distractii este: {suma_distractii}")

#Sfarsit problema 5