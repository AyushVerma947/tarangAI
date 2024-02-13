import numpy as np
import sounddevice as sd
import random
def r():
    # Function to generate a sinusoidal waveform for a given frequency and duration
    def generate_sine_wave(frequency, duration, sample_rate):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        return 0.5 * np.sin(2 * np.pi * frequency * t)

    # Set the duration and sample rate for the audio
    duration = 3  # seconds
    sample_rate = 44100  # samples per second

    # Initialize the mixed signal with zeros
    mixed_signal = np.zeros(int(duration * sample_rate))

    # Generate and mix two random frequencies between 20 and 20000 Hz
    frequency1 = random.uniform(20, 20000)
    frequency2 = random.uniform(20, 20000)

    sine_wave1 = generate_sine_wave(frequency1, duration, sample_rate)
    sine_wave2 = generate_sine_wave(frequency2, duration, sample_rate)

    mixed_signal = sine_wave1 + sine_wave2

    # Normalize the mixed signal to prevent clipping
    mixed_signal /= np.max(np.abs(mixed_signal))

    # Play the mixed frequencies simultaneously
    sd.play(mixed_signal, sample_rate)
    sd.wait()
    print(f' h Successfully played frequencies {frequency1} Hz and {frequency2} Hz.')