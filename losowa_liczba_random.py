import random

#losujemy liczbe z danego przedzialu

losowa= random.randint(1,10)
print("wynik losowania z liczb z zakresu 1 do 10 to:", losowa)

#losujemy 5 liczb losowych i zapisuje,y je do listy
liczba_1= int(input("podaj pierwsza liczbe"))
liczba_2= int(input("podaj druga liczbe"))
lista_losowych= random.sample(range(liczba_1, liczba_2), 5)

print(f"losta liczb losowanych z zakresu {liczba_1} do {liczba_2} to: {lista_losowych}")

