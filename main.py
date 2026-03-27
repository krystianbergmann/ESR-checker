from esr_utils import find_capacitor, evaluate_esr


def main():
    while True:
        user_input = input("Enter capacitor value in uF (or 'exit'): ")

        if user_input.lower() == "exit":
            print("Program closed.")
            break

        try:
            searched_capacitance = float(user_input)
        except ValueError:
            print("Please enter a valid number.")
            print("---")
            continue

        capacitor = find_capacitor(searched_capacitance)

        if capacitor is None:
            print("Capacitor value not found in the table.")
            print("---")
            continue

        print("Capacitance:", capacitor["capacitance"], "uF")
        print("ESR max:", capacitor["esr_max"], "Ohm")
        print("ESR Audio:", capacitor["esr_audio"], "Ohm")

        measured_input = input("Enter measured ESR in Ohm: ")

        try:
            measured_esr = float(measured_input)
        except ValueError:
            print("Please enter a valid ESR value.")
            print("---")
            continue

        result = evaluate_esr(measured_esr, capacitor)

        print("Measured ESR:", measured_esr, "Ohm")
        print("Result:", result)
        print("---")


if __name__ == "__main__":
    main()