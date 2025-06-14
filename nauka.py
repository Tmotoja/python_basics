from math import trunc

x = 5
print(f"siema oto wynik {x}")


import math

x= 90
print(f"podaje wynik cosinusa z liczby x: {math.cos(x)}")

print(f"obcinam wartosc po przecinku z wyniku: {trunc(math.cos(x))}")

x2= (trunc(math.cos(x)))

print(f"poteguje wartosc x do wyniku z cosinusa x: {pow(x, x2)}")

t= "Tomek"
j= " jest"
s= " super"

zdanie= t.strip() + j + s

print(zdanie)

slowa= ["elo", "czesc", "co tam"]


print(3*f"\t {slowa[2]}")

print("Alicja w krainie czarow" \
+ "-" \
+ "Alicja po drugiej stronie lustra")

for i in range(10, 19):
    print(f"| liczba {i} do kwadratu to: | {pow(i, 2):b} |")


imie="tomek"

print(len(imie))

print(imie [2:5])

name="tomek to imie"
print(name)

name_1= name.split()
print(name_1)

jezyki= ["python", "c++", "java"]
cyfry= [1,2,3,4,5,6,7,8,9,0]

print("jezyki programowania:")

for x in range(len(jezyki)):
    print(jezyki[x], end=" ")
print()

for x in range(len(cyfry)):
    print(f"({cyfry[x]}", end=" ")

print()
print(*cyfry)
print(*cyfry, sep="-")


komunikat= "Odmowil"

def pacjent(nr, imie, nazwisko):
    print(f"Pacjent numer {nr}, o imieniu: {imie}, i nazwisku: {nazwisko}")
print(pacjent(3, "tomek", "kowalski" ))

komunikat1 = "Bodybuilder"

print(type(komunikat1))
print( komunikat1.upper() )

s= "Tomek bedzie bodybuilderem"
liczba= "17"
print("Ciag \"17\" to liczba?", liczba.isdigit())

print(s.upper())
print(s.lower())
print(s.swapcase())

tytul= "\n\t\t** Nowy wspanialy steryd **\n"
print("Tytul:", tytul, len(tytul))

x= "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
print(x)

print("podmieniamy slowo 'wood' na 'drewno':")
print(x.replace("wood", "drewno"))


print("\n\t\t--ROZDZIAL: KLASY--")

class Complex():
    def __init__(self, pRe=0, pIm=0):
        self.re= pRe
        self.im= pIm
        print("Narodzil sie nowy obiekt...Nie zapomnij o deklaracji 500+")

    def __str__(self):
        return str(self.re) + "+" + str(self.im) + "i"

    def dodaj(self, x2):
        self.im = self.im + x2.im
        self.re = self.re + x2.re

print(Complex(2,5))

class Wiek_kota():
    def __init__(self, ludzkie_lata= 0):
        kocie_lata=  ludzkie_lata * 7
        print(f"{ludzkie_lata} ludzkich lat to {kocie_lata} lat kocich")

class Samochod():
    def __str__(self, marka, model, rocznik):
        self.marka= marka
        self.model= model
        self.rocznik= rocznik

    def dane(self, marka, model, rocznik):
        print(f"Oto samochod marki {marka}, model {model}, z rocznika {rocznik}")


print("\n\n\t\t --ROZDZIAL: KLASY PRO--")

import datetime
import math


class Pomiar(object):
    LimitNapiecia= 250
    Licznik= 0

    def __init__(self, pAutor, pOdczyt):
        self._dataczas= str(datetime.datetime.now() )[0:19]
        self._autor=pAutor

        if math.fabs(pOdczyt) <= Pomiar.LimitNapiecia:
            self._odczyt= pOdczyt

        else:

            raise Exception("Odczyt nie moze przekroczyc wartosci " + str(Pomiar.LimitNapiecia) + "V")

        Pomiar.Licznik+=1

    def __str__(self):
        return "odczyt="+ str(self._odczyt) +\
            " Dane kontrolne:|"+self._autor+"|"+self.dataczas

    @property
    def dataczas(self):
        return self._dataczas
    @property
    def autor(self):
        return self._autor
    @property
    def odczyt(self):
        return self._odczyt
    @odczyt.setter
    def odczyt(self, korekta):
        if math.fabs(korekta) <= Pomiar.LimitNapiecia:
            self._odczyt= korekta
        else:
            raise Exception("Odczyt nie moze przekroczyc wartosci " + str(Pomiar.LimitNapiecia) + "V")
    def komunikat(self):
            print("siema jestem obiektem klasy Pomiar")