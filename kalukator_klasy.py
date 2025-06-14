import math


class Kalkulator:

    def __init__(self, liczba_1, liczba_2):
        self.liczba_1= liczba_1
        self.liczba_2= liczba_2

    def dodawanie(self):
        return self.liczba_1 + self.liczba_2

    def odejmowanie(self):
        return self.liczba_1 - self.liczba_2

    def mnozenie(self):
        print(self.liczba_1*self.liczba_2)

    def dzielenie(self):
        print(self.liczba_1 /self.liczba_2)

    def potegowanie(self):
        return math.pow(self.liczba_1, self.liczba_2)

    def pierwiastkowanie(self):
        print(math.sqrt(self.liczba_1))


liczba_1= int(input("Podaj pierwsza liczbe:"))
liczba_2= int(input("Podaj druga liczbe:"))

dodawanie_1= Kalkulator(liczba_1, liczba_2)
print(dodawanie_1.dzielenie())
