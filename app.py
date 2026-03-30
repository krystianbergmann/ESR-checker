import streamlit as st
from esr_utils import (
    find_capacitor,
    evaluate_esr,
    get_available_capacitances,
    get_available_voltages,
    format_voltage,
    get_audio_threshold,
)

st.set_page_config(page_title="ESR Checker", page_icon="🔧")

st.title("ESR Checker")
st.write("Check approximate ESR reference values for electrolytic capacitors.")

available_capacitances = get_available_capacitances()

selected_capacitance = st.selectbox(
    "Select capacitor value (uF)",
    available_capacitances
)

available_voltages = get_available_voltages(selected_capacitance)

selected_voltage = st.selectbox(
    "Select capacitor voltage (V)",
    available_voltages,
    format_func=lambda v: format_voltage(v)
)

measured_esr = st.number_input(
    "Enter measured ESR (Ohm)",
    min_value=0.0,
    step=0.01,
    format="%.2f"
)

if st.button("Check capacitor"):
    capacitor = find_capacitor(selected_capacitance, selected_voltage)

    if capacitor is not None:
        audio_threshold = get_audio_threshold(capacitor)

        st.subheader("Reference values")
        st.write(f"**Capacitance:** {capacitor['capacitance']} uF")
        st.write(f"**Voltage:** {format_voltage(capacitor['voltage'])} V")
        st.write(f"**Reference ESR:** {capacitor['esr_reference']} Ohm")
        st.write(f"**Low-ESR / Audio threshold:** {audio_threshold} Ohm")

        result = evaluate_esr(measured_esr, capacitor)

        st.subheader("Result")
        st.write(f"**Measured ESR:** {measured_esr} Ohm")
        st.write(f"**Evaluation:** {result}")

        if result == "Low-ESR / Audio Standard":
            st.success("Capacitor meets the Low-ESR / Audio Standard.")
        elif result == "Acceptable":
            st.info("Capacitor is within the acceptable ESR range.")
        else:
            st.error("Capacitor is out of acceptable ESR range.")
    else:
        st.error("Capacitor value and voltage combination not found in the table.")