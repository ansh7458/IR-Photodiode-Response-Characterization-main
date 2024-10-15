# 📡 Characterization of IR Photodiode Response to IR LED Illumination

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Optics-IR_Sensing-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-Logistic_Fit-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Institute-NSUT-blue?style=for-the-badge" />
</p>

> **Centre for Electronic Design and Technology**  
> Netaji Subhas University of Technology, New Delhi  
> *Date: October 2024*

---

## 📋 Table of Contents
- [Synopsis](#-synopsis)
- [Introduction](#-introduction)
- [Block Diagram](#-block-diagram)
- [Procedure](#-procedure)
- [Model Fitting & Analysis](#-model-fitting--analysis)
- [Results](#-results)
- [Conclusion](#-conclusion)
- [Bill of Materials](#-bill-of-materials)

---

## 🎯 Synopsis

This experiment investigates the **current response of an IR photodiode** to illumination from an IR LED under controlled optical isolation. The LED current was systematically varied, and the resulting photodiode current was measured. The experimental data was fitted with a **logistic model** to capture the nonlinear response and saturation behavior. The results demonstrate the characteristic transition from **linear response** to a **saturation plateau**.

## 📖 Introduction

Infrared (IR) photodiodes are widely used in optoelectronic systems for detecting invisible infrared radiation. Applications include remote controls, optical communication, proximity sensing, and reflective object detection. Unlike simple photoconductive elements, photodiodes exhibit a **nonlinear current–light intensity relationship**. Accurately modeling this behavior is crucial for designing reliable IR sensing circuits.

## 🔧 Block Diagram

<p align="center">
  <img src="Block Diagram/" alt="Measurement Setup" width="600"/>
</p>

## ⚙️ Procedure

1. **Optical Isolation**: IR LED and photodiode mounted inside a black PVC tube (1" × 5cm), wrapped with black tape
2. **Mechanical Alignment**: Fixed 3 cm separation between LED and photodiode
3. **LED Current Control**: Variable DC supply with 100 Ω series resistor for current monitoring
4. **Photodiode Measurement**: Reverse-biased at 5V, current measured via 10 kΩ load resistor
5. **Dark Enclosure**: Entire assembly placed in closed cardboard box
6. **Data Analysis**: Python curve fitting with logistic model

## 📐 Model Fitting & Analysis

The photodiode response was modeled using a **logistic function**:

$$I_{PD} = \frac{I_{sat}}{1 + e^{-\alpha(I_{LED} - I_0)}}$$

Fitted parameters:
- **I_sat** = 510.79 µA (saturation current)
- **α** = 0.00055 per µA (steepness)
- **I₀** = 416.07 µA (midpoint LED current)

## 📊 Results

The response shows **rapid increase at low LED currents** and **saturates at approximately 510 µA** at high LED currents. The logistic model provides an excellent fit.

## ✅ Conclusion

The experiment successfully demonstrated the **nonlinear response** of a 5mm IR photodiode. The logistic model accurately captures both the rapid growth and saturation behavior. The extracted parameters offer a quantitative basis for **sensor calibration** in optical sensing systems.

## 📦 Bill of Materials

| S.No | Component | Value | Qty |
|------|-----------|-------|-----|
| 1 | IR Photodiode | 5mm | 1 |
| 2 | IR LED | 5mm (λₚ=940nm) | 1 |
| 3 | Resistor | 10 kΩ | 1 |
| 4 | Resistor | 100 Ω | 1 |
| 5 | Digital Multimeter | — | 1 |
| 6 | PVC Pipe | 2.5cm × 5cm | 1 |
| 7 | Cardboard Box | 15cm × 14cm | 1 |

## 🛠️ Technologies Used

`Python` · `SciPy` · `Matplotlib` · `NumPy`

## 👥 Authors
- **Ansh Gupta** — NSUT, New Delhi
- **Aditya Garg** — NSUT, New Delhi

---
*Centre for Electronic Design and Technology, NSUT, New Delhi*
