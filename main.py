from esr_utils import (
    find_capacitor,
    evaluate_esr,
    format_voltage,
    get_audio_threshold,
)


def main():
    while True:
        user_input = input("Enter capacitor value in uF (or 'exit'): ")

        if user_input.lower() == "exit":
            print("Program closed.")
            break

        try:
            searched_capacitance = float(user_input)
        except ValueError:
            print("Please enter a valid capacitance value.")
            print("---")
            continue

        voltage_input = input("Enter capacitor voltage in V: ")

        try:
            searched_voltage = float(voltage_input)
        except ValueError:
            print("Please enter a valid voltage value.")
            print("---")
            continue

        capacitor = find_capacitor(searched_capacitance, searched_voltage)

        if capacitor is None:
            print("Capacitor value and voltage combination not found in the table.")
            print("---")
            continue

        audio_threshold = get_audio_threshold(capacitor)

        print("Capacitance:", capacitor["capacitance"], "uF")
        print("Voltage:", format_voltage(capacitor["voltage"]), "V")
        print("Reference ESR:", capacitor["esr_reference"], "Ohm")
        print("Low-ESR / Audio threshold:", audio_threshold, "Ohm")

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