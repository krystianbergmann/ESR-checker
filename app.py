import streamlit as st
from esr_utils import find_capacitor, evaluate_esr, get_available_capacitances


st.set_page_config(page_title="ESR Checker", page_icon="🔧")

st.title("ESR Checker")
st.write("Check approximate ESR reference values for electrolytic capacitors.")

available_capacitances = get_available_capacitances()

selected_capacitance = st.selectbox(
    "Select capacitor value (uF)",
    available_capacitances
)

measured_esr = st.number_input(
    "Enter measured ESR (Ohm)",
    min_value=0.0,
    step=0.01,
    format="%.2f"
)

if st.button("Check capacitor"):
    capacitor = find_capacitor(selected_capacitance)

    if capacitor is not None:
        st.subheader("Reference values")
        st.write(f"**Capacitance:** {capacitor['capacitance']} uF")
        st.write(f"**ESR max:** {capacitor['esr_max']} Ohm")
        st.write(f"**ESR Audio:** {capacitor['esr_audio']} Ohm")

        result = evaluate_esr(measured_esr, capacitor)

        st.subheader("Result")
        st.write(f"**Measured ESR:** {measured_esr} Ohm")
        st.write(f"**Evaluation:** {result}")

        if measured_esr <= capacitor["esr_audio"]:
            st.success("Very good condition - suitable for audio use.")
        elif measured_esr <= capacitor["esr_max"]:
            st.warning("Capacitor is acceptable.")
        else:
            st.error("Capacitor is out of acceptable range.")
    else:
        st.error("Capacitor value not found in the table.")