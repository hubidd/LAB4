import sys

def czytaj_linie(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as f:
        for linia in f:
            yield linia.strip()

def filtruj_logi(gen, poziom):
    for linia in gen:
        if poziom in linia:
            yield linia

def licz_statystyki(gen):
    stat = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}
    for linia in gen:
        for klucz in stat:
            if klucz in linia:
                stat[klucz] += 1
        yield stat

linie = [linia.strip() for linia in open("log.txt")]
print("Lista:", sys.getsizeof(linie))

gen = czytaj_linie("log.txt")
print("Generator:", sys.getsizeof(gen))

gen_linii = czytaj_linie("log.txt")
gen_error = filtruj_logi(gen_linii, "ERROR")
for linia in gen_error:
    print(linia)

gen_linii = czytaj_linie("log.txt")
gen_stat = licz_statystyki(gen_linii)

final_stat = None
for stat in gen_stat:
    final_stat = stat

print(final_stat)