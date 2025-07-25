import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.62607015e-34  # Planck's constant (Joule second)
c = 3e8  # Speed of light (meters per second)
k_B = 1.380649e-23  # Boltzmann's constant (Joule per Kelvin)
T = 3000  # Temperature in Kelvin

# Wavelength range (meters)
wavelengths = np.linspace(1e-9, 3e-6, 1000)

# Wien's distribution
def wien_law(lambda_, T):
    return (2 * h * c**2) / (lambda_**5) * np.exp(-h * c / (lambda_ * k_B * T))

# Rayleigh-Jeans distribution
def rayleigh_jeans_law(lambda_, T):
    return (2 * c * k_B * T) / (lambda_**4)

# Planck's distribution
def planck_law(lambda_, T):
    return (2 * h * c**2) / (lambda_**5) / (np.exp(h * c / (lambda_ * k_B * T)) - 1)

# Compute spectral radiance for each law
wien_radiance = wien_law(wavelengths, T)
rayleigh_jeans_radiance = rayleigh_jeans_law(wavelengths, T)
planck_radiance = planck_law(wavelengths, T)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(wavelengths * 1e9, wien_radiance, label="Wien's Law", color='red')
plt.plot(wavelengths * 1e9, rayleigh_jeans_radiance, label="Rayleigh-Jeans Law", color='blue')
plt.plot(wavelengths * 1e9, planck_radiance, label="Planck's Law", color='green')
plt.yscale('log')
plt.xlabel('Wavelength (nm)')
