class Pies:
    """klasa reprezentujaca psa"""
    def __init__(self, imie, wiek):
        """"konstruktor"""
        self.imie= imie
        self.wiek= wiek

    def szczekanie(self):
        """metoda pies szczeka"""
        print(f"{self.imie} szczeka: Whoof Whoof")

    def przelicz_wiek(self):
        """metoda: zwraca ludzki wiek psa"""
        return self.wiek*7

pies_1= Pies("bartek", 5)

pies_1.szczekanie()
print(pies_1.wiek)
print(pies_1.przelicz_wiek())

print(pies_1.szczekanie())