import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
def con(f1,f2):

    # Function to convolve two signals
    def convolve_signals(signal1, signal2):
        return np.convolve(signal1, signal2, 'full')

    # Input from the user
    frequency1 = f1
    frequency2 = f2
    # Create time-domain signals for the input frequencies
    fs = 44100  # Sampling frequency (Hz)
    t = np.arange(0, 1, 1/fs)  # Time values from 0 to 1 second
    signal1 = np.sin(2 * np.pi * frequency1 * t)
    signal2 = np.sin(2 * np.pi * frequency2 * t)

    # Convolve the two signals
    convolved_signal = convolve_signals(signal1, signal2)

    # Normalize the convolved signal to prevent clipping
    convolved_signal /= np.max(np.abs(convolved_signal))

    # Play the convolved signal
    print("Playing the convolved signal...")
    sd.play(convolved_signal, fs)
    sd.wait()
    print("Playback finished.")