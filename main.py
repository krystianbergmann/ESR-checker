from esr_data import esr_table
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