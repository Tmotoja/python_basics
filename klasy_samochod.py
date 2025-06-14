class Samochod:
    #definicja klasy
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.predkosc = 0
        self.wlaczony_silnik = False

    def uruchom_silnik(self):
        print("silnik zostal uruchomiony")
        self.wlaczony_silnik = True

    def przyspiesz(self, wartosc):
        self.predkosc += wartosc

moj_samochod = Samochod("Toyota", "Yaris")
moj_samochod.uruchom_silnik()
moj_samochod.przyspiesz(30)

moj_samochod_2 = Samochod("BMW", "M3")
print(moj_samochod_2.predkosc)
print(moj_samochod.marka)
print(moj_samochod.model)