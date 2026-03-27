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


def evaluate_esr(measured_esr, capacitor):
    if measured_esr <= capacitor["esr_reference"]:
        return "Acceptable"
    else:
        return "Out of acceptable range"


def get_available_capacitances():
    return sorted(esr_table.keys())


def get_available_voltages(capacitance):
    if capacitance in esr_table:
        return sorted(esr_table[capacitance].keys())
    return []