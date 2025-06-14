#cwiczenie2

def stworz_album(artysta, album, liczba_utworow=None):
    slownik = {
        "artysta": artysta,
        "album": album
    }
    if liczba_utworow is not None:
        slownik["liczba_utworow"] = liczba_utworow
    return slownik

wynik = stworz_album("Rihanna", "Diamonds", 12)
print(wynik)