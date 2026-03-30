## Streamlit as a Lightweight UI Layer for Hardware Diagnostics

This project explores whether **Streamlit** can serve as a practical interface layer for real-time hardware diagnostics.

Rather than focusing on building a perfect measurement tool, the goal is to validate a broader technological question:

> Can Streamlit be effectively used to prototype and operate simple diagnostic systems without investing in a full frontend stack?

To answer this, a minimal ESR (Equivalent Series Resistance) measurement system was implemented and integrated with a Streamlit-based interface. This setup simulates a realistic scenario where engineers need fast, usable tooling to observe and interact with hardware signals.

The project evaluates:
- how quickly a functional UI can be built
- how well Streamlit handles interaction with hardware data
- whether the resulting interface is sufficient for real-world usage

This is not a production system.

It is a **decision-oriented experiment** designed to understand where Streamlit provides real value — and where its limitations make it unsuitable.

## Overview
ESR Checker is a simple Python project for checking approximate ESR reference values of electrolytic capacitors based on capacitance.

It was created as a learning project that combines basic Python programming with practical capacitor diagnostics. The application allows the user to enter a capacitor value manually and compare it with reference ESR values stored in a predefined table.

The project now includes both:
- a **console version** for basic terminal interaction
- a **web interface built with the Streamlit library**

Streamlit makes it possible to run the project as a simple local web application with a more user-friendly interface.

## Features

- ESR reference lookup based on capacitance and voltage
- support for voltage-dependent capacitor ESR values
- measured ESR comparison with reference ESR data
- console-based workflow for repeated checks
- simple and user-friendly web interface built with **Streamlit**
- clean, modular, and beginner-friendly code structure

## Project Purpose

This project is intended to provide a simple way to check whether a capacitor's ESR is still within an acceptable range.

At the same time, it serves as a practical Python learning exercise focused on:

- lists and dictionaries
- loops
- user input
- basic lookup logic
- small project organization
- separating application logic from the user interface
- building a simple UI with Streamlit

## Streamlit Interface

In addition to the console version, this project also includes a simple user interface built with the **Streamlit** library.

Streamlit allows the application to run in the browser as a lightweight local web app. It provides a more convenient way to interact with the ESR checker without using terminal input commands.

## About ESR

**ESR** stands for **Equivalent Series Resistance**.

It is one of the most important parameters used when evaluating the condition of an electrolytic capacitor. A capacitor may still measure close to its nominal capacitance, but if its ESR is too high, it can already be degraded and may no longer perform correctly in a real circuit.

High ESR may indicate:
- capacitor aging
- electrolyte drying
- reduced filtering performance
- poor behavior under load

This is especially important in:
- power supply circuits
- filtering stages
- amplifier circuits
- audio equipment
- restoration and repair work 

## ESR Reference Levels Used in This Project

This project uses two reference values for each capacitance:

### ESR max
The maximum acceptable ESR value for a given capacitor value.

If the measured ESR is higher than this level, the capacitor should be considered out of acceptable range.

### ESR Audio
A stricter ESR reference intended for audio-related applications.

In many audio circuits, lower ESR is preferred for better stability and performance, especially in:
- audio power supply filtering
- amplifier support circuits
- restoration of vintage audio equipment
- situations where component quality is more critical

## Important Note

The ESR values used in this project are **approximate reference values**.

They are intended for:
- learning purposes
- quick comparison
- basic ESR interpretation

They are **not manufacturer-specific specifications** and should not be treated as a replacement for datasheet values.

In real-world applications, ESR can also depend on:
- capacitor voltage rating
- temperature
- capacitor series and construction
- measurement frequency
- whether the capacitor is a general-purpose, low-ESR, audio-grade, or polymer type

Some values in this project are based on published reference lookup charts and should be treated as practical guidance rather than universal limits.

## Voltage-Dependent ESR Reference Table

The table below contains approximate ESR reference values used by the application.  
Values depend on both capacitor capacitance and voltage rating.

| Capacitance (uF) | 6.3V | 10V | 16V | 25V | 35V | 63V | 100V | 250V |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | - | - | - | - | 14 | 16 | 18 | 20 |
| 2.2 | - | - | - | 6.0 | 8.0 | 10 | 10 | 18 |
| 4.7 | 62 | - | - | 15 | 7.5 | 4.2 | 2.3 | 5.0 |
| 10 | 29 | - | 8.0 | 5.3 | 3.2 | 2.4 | 3.0 | 2.5 |
| 22 | 13 | 5.4 | 3.6 | 2.1 | 1.5 | 1.5 | 1.5 | 1.8 |
| 47 | 6.2 | 2.2 | 1.6 | 1.2 | 0.68 | 0.56 | 0.7 | 0.8 |
| 100 | 2.9 | 1.2 | 0.7 | 0.32 | 0.32 | 0.3 | 0.15 | 0.8 |
| 220 | 1.3 | 0.6 | 0.33 | 0.23 | 0.17 | 0.16 | 0.09 | 0.5 |
| 470 | 0.62 | 0.24 | 0.18 | 0.12 | 0.09 | 0.09 | 0.05 | 0.3 |
| 1000 | 0.29 | 0.12 | 0.09 | 0.08 | 0.07 | 0.05 | 0.06 | - |
| 2200 | 0.16 | - | - | - | - | - | - | - |
| 4700 | 0.09 | 0.23 | 0.20 | 0.12 | 0.08 | 0.04 | - | - |
| 10000 | 0.06 | 0.12 | 0.08 | 0.06 | 0.04 | - | - | - |
| 22000 | 0.04 | - | - | - | - | - | - | - |
## Result Interpretation

A measured ESR value can be interpreted like this:

- **ESR <= ESR Audio** → very good condition, suitable for audio use
- **ESR Audio < ESR <= ESR max** → acceptable condition
- **ESR > ESR max** → out of acceptable range

## How to Run

### Console version

Run the console version from the project directory:

```bash
python main.py
```

### Streamlit version
```bash
streamlit run app.py
```

Run the Streamlit interface from the project directory:
## Project Structure

```text
esr-checker/
├── .gitignore
├── README.md
├── LICENSE
├── main.py
├── esr_data.py
└── tests/
    └── test_main.py
```

## Changelog

```md
## Changelog

### v0.6.0
- updated the Streamlit gauge to display ESR in Ohms (Ω) instead of a percentage-like score
- added visual thresholds on the gauge to show Low-ESR (audio) vs acceptable vs out-of-range ESR regions
- improved gauge scaling with a dynamic axis range so measured ESR and thresholds are always visible

### v0.5.0
- added support for 6.3V capacitor ESR reference values
- updated the ESR table with additional low-voltage entries
- updated the console version to support float voltage input
- updated the Streamlit interface to handle 6.3V values correctly
- improved voltage formatting in both console and Streamlit versions
- updated README documentation and ESR reference table

### v0.4.0
- updated the ESR table to support voltage-dependent reference values
- replaced the previous simplified capacitance-only ESR model
- updated the console version to ask for both capacitance and voltage
- updated the Streamlit interface to support voltage selection
- refactored lookup logic to work with capacitance and voltage pairs
- replaced `ESR max` / `ESR Audio` output with a voltage-based ESR reference value

### v0.3.0
- added Streamlit user interface
- added `app.py`
- moved ESR logic to `esr_utils.py`
- added ESR evaluation based on measured value
- improved project structure

### v0.2.0
- moved ESR table to `esr_data.py`
- added function-based code structure
- improved readability and maintainability

### v0.1.0
- initial console version
- added ESR lookup by capacitance
- added README, LICENSE, and `.gitignore`
```