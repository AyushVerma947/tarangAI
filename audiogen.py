import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import pandas as pd

def pitch_to_freq(pitch):
    return 440 * (2 ** ((pitch - 69) / 12))

def generate_sine_wave(duration, frequency=440, amplitude=0.5, sample_rate=44100):
    # Generate time array
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Generate sine wave
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)
    # Convert to 16-bit integers
    sine_wave = np.array(32767 * sine_wave, dtype=np.int16)
    return sine_wave

def play_generated_notes(generated_notes):
    # Create an empty audio segment
    audio = AudioSegment.empty()

    # Add notes to the audio segment
    for _, row in generated_notes.iterrows():
        pitch = int(row['pitch'])
        duration = row['duration']
        frequency = pitch_to_freq(pitch)
        amplitude = 0.5  # Adjust as needed
        sample_rate = 44100
        sine_wave = generate_sine_wave(duration, frequency, amplitude, sample_rate)
        note_audio = AudioSegment(sine_wave.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)
        audio = audio.append(note_audio, crossfade=0)

    # Normalize the audio data
    audio = audio.set_frame_rate(sample_rate).set_channels(1)

    # Play the audio using pydub's play function
    play(audio)

# # Example usage
# # Assuming generated_notes is a pandas DataFrame with columns 'pitch', 'step', 'duration', 'start', 'end'
# # Replace this with your actual DataFrame
# generated_notes = pd.DataFrame({
#     'pitch': [60, 62, 64, 65],
#     'step': [0.1, 0.2, 0.3, 0.4],
#     'duration': [0.5, 0.5, 0.5, 0.5],
#     'start': [0, 1, 2, 3],
#     'end': [0.5, 1.5, 2.5, 3.5]
# })
# #kuch run hua tha abhi??nahihaan music play hua,ok.
# # Play the generated notes
# play_generated_notes(generated_notes)