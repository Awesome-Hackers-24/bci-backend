import numpy as np
from scipy.signal import welch  # For spectral analysis
from scipy.fft import fft  # Fast Fourier Transform

def calculate_band_power(data, sf):
    """Calculate EEG band power using Welch's method"""
    freqs, psd = welch(data, sf)
    band_frequencies = {
        'Delta': (0.5, 4),
        'Theta': (4, 8),
        'Alpha': (8, 12),
        'Beta': (12, 30),
        'Gamma': (30, 45)
    }
    band_powers = {}
    for band, (low, high) in band_frequencies.items():
        idx_band = np.logical_and(freqs >= low, freqs <= high)
        band_power = np.sum(psd[idx_band])
        band_powers[band] = band_power
    return band_powers

def calculate_concentration(band_powers):
    """Calculate concentration based on band powers"""
    total_power = np.sum(list(band_powers.values()))
    beta_power = band_powers['Beta']
    concentration = (beta_power / total_power) * 100
    return concentration

# Example EEG data (randomly generated for demonstration)
np.random.seed(0)
sf = 256  # Sampling frequency in Hz
eeg_data = np.random.randn(2560)  # Simulated raw EEG data

# Calculate band powers
band_powers = calculate_band_power(eeg_data, sf)

# Calculate concentration
concentration = calculate_concentration(band_powers)
print("Concentration Level: {:.2f}%".format(concentration))
