#zwracanie

def miasta_panstwa(miasto, ludnosc = 0, panstwo = ("Polska")):
    """ Funkcja kalkulatora ktory sumuje liczby """
    if ludnosc == 0:
        ludnosc = "NaN"

    miasto_panstwo_slownik = {"panstwo": panstwo, "ludnosc": ludnosc, "miasto": miasto}
    return miasto_panstwo_slownik


miasto_funkcja = miasta_panstwa("Paryz", 0, "Francja")
print(miasto_funkcja)
