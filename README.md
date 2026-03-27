# ESR Checker

A simple Python console application for checking approximate ESR values of electrolytic capacitors based on capacitance.

This project is intended as a learning project for Python and basic capacitor diagnostics. It allows the user to manually enter a capacitor value and display reference ESR limits from a predefined table.

## Features

- manual capacitor value input from the console
- ESR reference lookup based on capacitance
- separate **ESR max** and **ESR Audio** reference levels
- continuous loop mode for repeated checks
- simple and beginner-friendly code structure

## Project Purpose

The goal of this project is to provide a simple tool for checking whether the ESR value of an electrolytic capacitor is within an acceptable range.

It is also designed as a beginner-friendly Python project, focusing on:
- lists and dictionaries
- loops
- user input
- basic data lookup
- simple project structure

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

The ESR values used in this project are **simplified reference values**.

They are intended for:
- learning purposes
- quick comparison
- basic ESR interpretation

They are **not manufacturer-specific specifications** and should not be treated as exact replacement for datasheet values.

In real-world applications, ESR can also depend on:
- capacitor voltage rating
- temperature
- capacitor series and construction
- measurement frequency
- whether the capacitor is a general-purpose, low-ESR, audio-grade, or polymer type

## ESR Reference Table

| Capacitance (uF) | ESR max (Ohm) | ESR Audio (Ohm) |
|---:|---:|---:|
| 1 | 15.0 | 10.0 |
| 2.2 | 10.0 | 6.0 |
| 4.7 | 5.0 | 3.0 |
| 10 | 3.0 | 2.0 |
| 22 | 2.0 | 1.0 |
| 47 | 1.0 | 0.7 |
| 100 | 0.8 | 0.5 |
| 220 | 0.5 | 0.3 |
| 470 | 0.3 | 0.2 |
| 1000 | 0.2 | 0.12 |
| 2200 | 0.1 | 0.08 |

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

Dodaj na końcu README:

```md
## Changelog

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

