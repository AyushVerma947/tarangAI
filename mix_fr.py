import numpy as np
import sounddevice as sd

def play_mixed_audio(frequency1, frequency2, duration=2, sample_rate=44100):
    # Generate time values
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Ensure the frequency values are of the float data type
    frequency1 = float(frequency1)
    frequency2 = float(frequency2)

    # Generate sine waves for each frequency
    wave1 = np.sin(2 * np.pi * frequency1 * t)
    wave2 = np.sin(2 * np.pi * frequency2 * t)

    # Mix the two audio signals
    mixed_wave = wave1 + wave2

    # Play the mixed audio
    sd.play(mixed_wave, sample_rate)
    sd.wait()

