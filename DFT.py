import numpy as np
import matplotlib.pyplot as plt

# Signal array (change as needed)
#signal = []


signal2 = [0.0, 0.309, 0.588, 0.809, 0.9511, 1.0, 0.9511, 0.809, 0.588, 0.309,
0.0, -0.309, -0.588, -0.809, -0.9511, -1.0, -0.9511, -0.809, -0.588, -0.309,
0.0, 0.309, 0.588, 0.809, 0.9511, 1.0, 0.9511, 0.809, 0.588, 0.309,
0.0, -0.309, -0.588, -0.809, -0.9511, -1.0, -0.9511, -0.809, -0.588, -0.309,
0.0, 0.309, 0.588, 0.809, 0.9511, 1.0, 0.9511, 0.809, 0.588, 0.309,
0.0, -0.309, -0.588, -0.809, -0.9511, -1.0, -0.9511, -0.809, -0.588, -0.309,
0.0, 0.309, 0.588, 0.809, 0.9511, 1.0, 0.9511, 0.809, 0.588, 0.309,
0.0, -0.309, -0.588, -0.809, -0.9511, -1.0, -0.9511, -0.809, -0.588, -0.309,
0.0, 0.309, 0.588, 0.809, 0.9511, 1.0, 0.9511, 0.809, 0.588, 0.309,
0.0, -0.309, -0.588, -0.809, -0.9511, -1.0, -0.9511, -0.809, -0.588, -0.309,

]



signal = [25,25,25,27,25,25,79,25,25,79,102,25]


avg = np.mean(signal)
print(avg)


# FFT
N = len(signal)
dft_result = np.fft.fft(signal)
freq = np.fft.fftfreq(N)
amplitude = np.abs(dft_result)

# 🎯 Print Frequency and Amplitude with units
print("Frequency (Hz)\tAmplitude")
for f, a in zip(freq, amplitude):
    print(f"{f:.2f} Hz\t\t{a:.2f}")

# Plot
plt.figure(figsize=(10, 5))
(markerline, stemlines, baseline) = plt.stem(freq, amplitude)
plt.setp(markerline, 'markerfacecolor', 'b')
plt.title('DFT (using FFT) - Amplitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
