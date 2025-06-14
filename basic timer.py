import time #zimportowany modul

def slow_function():
    print("Rozpoczynam zadanie slow_function")
    time.sleep(3) #program stoi przez 3 sekundy
    print("Zakonczylem dzialanie slow_function")

print("Zaczynam pomiar czasu")
start_time = time.time()

slow_function()

end_time = time.time() #zancznik czasu w momencie rozpoczecia dzialania pomiaru

elapsed_time = end_time - start_time #roznica czasu

print(f"Funkcja dokonala sie w czasie {elapsed_time} sekund")