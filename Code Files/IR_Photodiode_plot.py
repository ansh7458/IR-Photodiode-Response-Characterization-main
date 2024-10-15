import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# -----------------------
# Load data
# -----------------------
data = np.loadtxt("IR_Photodiode_characteristics.csv", delimiter=",", skiprows=1)
I_LED = data[:, 0]  # IR LED current (µA)
I_PD = data[:, 1]   # Photodiode current (µA)

# -----------------------
# Logistic model
# -----------------------
def logistic_model(I, Isat, alpha, I0):
    return Isat / (1 + np.exp(-alpha * (I - I0)))

# -----------------------
# Fit logistic model
# -----------------------
popt, pcov = curve_fit(logistic_model, I_LED, I_PD, p0=[510, 0.001, 100])
Isat_fit, alpha_fit, I0_fit = popt
# -----------------------
# Generate fitted curve
# -----------------------
I_fit = np.linspace(min(I_LED), max(I_LED), 1000)
I_PD_fit = logistic_model(I_fit, *popt)

# -----------------------
# Plot results
# -----------------------
plt.figure(figsize=(9,6))
plt.scatter(I_LED, I_PD, color='blue', s=35, label="Measured Data")
plt.plot(I_fit, I_PD_fit, 'r-', linewidth=2,
         label=rf"Logistic Fit: $I_{{PD}} = \frac{{{Isat_fit:.1f}}}{{1 + e^{{-{alpha_fit:.4f}(I - {I0_fit:.1f})}}}}$")

plt.xlabel("IR LED Current (µA)", fontsize=12)
plt.ylabel("Photodiode Current (µA)", fontsize=12)
plt.title("IR Photodiode Response vs IR LED Current", fontsize=14)
plt.grid(True, ls="--", alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# -----------------------
# Print fitted parameters
# -----------------------
print("===== Logistic Fit Parameters =====")
print(f"Isat = {Isat_fit:.2f} µA")
print(f"alpha = {alpha_fit:.5f} per µA")
print(f"I0 (midpoint) = {I0_fit:.2f} µA")
