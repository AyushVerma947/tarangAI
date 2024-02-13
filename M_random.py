import random
import numpy as np
import sounddevice as sd
def play(ch):
    # Define the frequency dictionaries for different bands
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

    if ch=="A_band":
        selected_band = A_band
    elif ch=="B_band":
        selected_band = B_band
    elif ch=="C_band":
        selected_band = C_band
    elif ch=="D_band":
        selected_band = D_band
    elif ch=="E_band":
        selected_band = E_band
    elif ch=="F_band":
        selected_band = F_band
    elif ch=="G_band":
        selected_band = G_band
    
        
    # Select a band (e.g., A_band or B_band)
    

    # List of notes in the selected band
    notes = list(selected_band.keys())

    # Number of notes to play
    num_notes_to_play = 10  # Adjust as needed

    # Sample rate and note duration
    sample_rate = 44100
    note_duration_ms = 500

    # Play random notes from the selected band
    for _ in range(num_notes_to_play):
        random_note = random.choice(notes)
        frequency = selected_band.get(random_note)

        t = np.linspace(0, note_duration_ms / 1000, int(note_duration_ms * sample_rate / 1000), endpoint=False)
        sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

        sd.play(sine_wave, sample_rate)
        sd.wait()
