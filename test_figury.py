import figury
from figury import Kwadrat

dlugosc_boku_1 = 3

kwadrat_pow = Kwadrat(dlugosc_boku_1)


print(f"Pole kwadratu o boku {dlugosc_boku_1} to:{kwadrat_pow.powierzchnia()}")

from figury import Kolo

promien_1= 3

kolo_pow= Kolo(promien_1)

print(f"Pole kola o promieniu {promien_1} to: {kolo_pow.powierzchnia()}")
