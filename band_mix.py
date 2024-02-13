import numpy as np
import sounddevice as sd
import random
def r():
    # Function to generate a sinusoidal waveform for a given frequency and duration
    def generate_sine_wave(frequency, duration, sample_rate):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        return 0.5 * np.sin(2 * np.pi * frequency * t)

    # Define the frequency dictionaries
    A_band = {
        'Sa': 32,
        'Re': 36,
        'Ga': 41,
        'Ma': 43,
        'Pa': 48,
        'Dha': 55,
        'Ni': 61
    }

    B_band = {
        'Sa': 65,
        'Re': 73,
        'Ga': 82,
        'Ma': 87,
        'Pa': 98,
        'Dha': 110,
        'Ni': 123
    }

    C_band = {
        'Sa': 261,
        'Re': 293,
        'Ga': 329,
        'Ma': 349,
        'Pa': 392,
        'Dha': 440,
        'Ni': 493
    }

    D_band = {
        'Sa': 261,
        'Re': 293,
        'Ga': 329,
        'Ma': 350,
        'Pa': 392,
        'Dha': 440,
        'Ni': 493
    }

    E_band = {
        'Sa': 329.63,
        'Re': 369.99,
        'Ga': 415.30,
        'Ma': 720,
        'Pa': 784,
        'Dha': 880,
        'Ni': 987
    }

    F_band = {
        'Sa': 1046,
        'Re': 1174,
        'Ga': 1318,
        'Ma': 1396,
        'Pa': 1568,
        'Dha': 1760,
        'Ni': 1979
    }

    G_band = {
        'Sa': 2093,
        'Re': 2349,
        'Ga': 2637,
        'Ma': 2793,
        'Pa': 3136,
        'Dha': 3520,
        'Ni': 3951,
        'saa': 4186
    }

    # Combine all the bands into a list
    bands = [A_band, B_band, C_band, D_band, E_band, F_band, G_band]

    # Randomly choose two different bands
    selected_bands = random.sample(bands, 2)

    # Randomly select two notes from the selected bands
    selected_notes = [random.choice(list(selected_bands[0].keys())), random.choice(list(selected_bands[1].keys()))]

    # Get the frequencies of the selected notes
    freq1 = selected_bands[0][selected_notes[0]]
    freq2 = selected_bands[1][selected_notes[1]]

    # Set the duration and sample rate for the audio
    duration = 3  # seconds
    sample_rate = 44100  # samples per second

    # Initialize the mixed signal with zeros
    mixed_signal = np.zeros(int(duration * sample_rate))

    # Generate sine waves for the selected frequencies
    sine_wave1 = generate_sine_wave(freq1, duration, sample_rate)
    sine_wave2 = generate_sine_wave(freq2, duration, sample_rate)

    # Mix the sine waves
    mixed_signal = sine_wave1 + sine_wave2

    # Normalize the mixed signal to prevent clipping
    mixed_signal /= np.max(np.abs(mixed_signal))

    # Play the mixed frequencies simultaneously
    sd.play(mixed_signal, sample_rate)
    sd.wait()

    print(f"Successfully played frequencies {selected_notes[0]} ({freq1} Hz) and {selected_notes[1]} ({freq2} Hz) from different bands.")
