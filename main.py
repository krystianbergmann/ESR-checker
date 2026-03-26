from esr_data import esr_table

def find_capacitor(capacitance):
    for capacitor in esr_table:
        if capacitor["capacitance"] == capacitance:
            return capacitor
    return None


def main():
    while True:
        user_input = input("Enter capacitor value in uF (or 'exit'): ")

        if user_input.lower() == "exit":
            print("Program closed.")
            break

        searched_capacitance = float(user_input)

        capacitor = find_capacitor(searched_capacitance)

        if capacitor is not None:
            print("Capacitance:", capacitor["capacitance"], "uF")
            print("ESR max:", capacitor["esr_max"], "Ohm")
            print("ESR Audio:", capacitor["esr_audio"], "Ohm")
            print("---")
        else:
            print("Capacitor value not found in the table.")
            print("---")


if __name__ == "__main__":
    main()