from esr_data import esr_table


def find_capacitor(capacitance, voltage):
    if capacitance in esr_table:
        if voltage in esr_table[capacitance]:
            return {
                "capacitance": capacitance,
                "voltage": voltage,
                "esr_reference": esr_table[capacitance][voltage]
            }
    return None


def get_audio_threshold(capacitor):
    return round(capacitor["esr_reference"] * 0.7, 2)


def evaluate_esr(measured_esr, capacitor):
    audio_threshold = get_audio_threshold(capacitor)
    reference_esr = capacitor["esr_reference"]

    if measured_esr <= audio_threshold:
        return "Low-ESR / Audio Standard"
    elif measured_esr <= reference_esr:
        return "Acceptable"
    else:
        return "Out of acceptable range"


def get_available_capacitances():
    return sorted(esr_table.keys())


def get_available_voltages(capacitance):
    if capacitance in esr_table:
        return sorted(esr_table[capacitance].keys())
    return []


def format_voltage(voltage):
    if voltage == int(voltage):
        return str(int(voltage))
    return str(voltage)