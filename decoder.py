esr_table = [
    {"capacitance": 1, "esr_max": 15.0, "esr_audio": 10.0},
    {"capacitance": 2.2, "esr_max": 10.0, "esr_audio": 6.0},
    {"capacitance": 4.7, "esr_max": 5.0, "esr_audio": 3.0},
    {"capacitance": 10, "esr_max": 3.0, "esr_audio": 2.0},
    {"capacitance": 22, "esr_max": 2.0, "esr_audio": 1.0},
    {"capacitance": 47, "esr_max": 1.0, "esr_audio": 0.7},
    {"capacitance": 100, "esr_max": 0.8, "esr_audio": 0.5},
    {"capacitance": 220, "esr_max": 0.5, "esr_audio": 0.3},
    {"capacitance": 470, "esr_max": 0.3, "esr_audio": 0.2},
    {"capacitance": 1000, "esr_max": 0.2, "esr_audio": 0.12},
    {"capacitance": 2200, "esr_max": 0.1, "esr_audio": 0.08}
]

while True:
    user_input = input("Enter capacitor value in uF (or 'exit'): ")

    if user_input.lower() == "exit":
        print("Program closed.")
        break

    searched_capacitance = float(user_input)
    found = False

    for capacitor in esr_table:
        if capacitor["capacitance"] == searched_capacitance:
            print("Capacitance:", capacitor["capacitance"], "uF")
            print("ESR max:", capacitor["esr_max"], "Ohm")
            print("ESR Audio:", capacitor["esr_audio"], "Ohm")
            print("---")
            found = True
            break

    if not found:
        print("Capacitor value not found in the table.")
        print("---")