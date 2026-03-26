tabela_esr = [
    {"pojemnosc": 1, "esr_max": 15.0, "esr_audio": 10.0},
    {"pojemnosc": 2.2, "esr_max": 10.0, "esr_audio": 6.0},
    {"pojemnosc": 4.7, "esr_max": 5.0, "esr_audio": 3.0},
    {"pojemnosc": 10, "esr_max": 3.0, "esr_audio": 2.0},
    {"pojemnosc": 22, "esr_max": 2.0, "esr_audio": 1.0},
    {"pojemnosc": 47, "esr_max": 1.0, "esr_audio": 0.7},
    {"pojemnosc": 100, "esr_max": 0.8, "esr_audio": 0.5},
    {"pojemnosc": 220, "esr_max": 0.5, "esr_audio": 0.3},
    {"pojemnosc": 470, "esr_max": 0.3, "esr_audio": 0.2},
    {"pojemnosc": 1000, "esr_max": 0.2, "esr_audio": 0.12},
    {"pojemnosc": 2200, "esr_max": 0.1, "esr_audio": 0.08}
]

while True:
    wpis = input("Podaj pojemność kondensatora w uF (lub 'koniec'): ")

    if wpis.lower() == "koniec":
        print("Koniec programu.")
        break

    szukana_pojemnosc = float(wpis)
    znaleziono = False

    for kondensator in tabela_esr:
        if kondensator["pojemnosc"] == szukana_pojemnosc:
            print("Pojemność:", kondensator["pojemnosc"], "uF")
            print("ESR max:", kondensator["esr_max"], "Ohm")
            print("ESR Audio:", kondensator["esr_audio"], "Ohm")
            print("---")
            znaleziono = True
            break

    if not znaleziono:
        print("Nie znaleziono takiej pojemności w tabeli.")
        print("---")