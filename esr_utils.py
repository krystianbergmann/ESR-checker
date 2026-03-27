from esr_data import esr_table


def find_capacitor(capacitance):
    for capacitor in esr_table:
        if capacitor["capacitance"] == capacitance:
            return capacitor
    return None


def evaluate_esr(measured_esr, capacitor):
    if measured_esr <= capacitor["esr_audio"]:
        return "Very good - suitable for audio use"
    elif measured_esr <= capacitor["esr_max"]:
        return "Acceptable"
    else:
        return "Out of acceptable range"


def get_available_capacitances():
    return [capacitor["capacitance"] for capacitor in esr_table]