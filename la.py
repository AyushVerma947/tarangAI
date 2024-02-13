import numpy as np
from scipy.io import wavfile
def mix(f1,f2): 
    # Step 1: Read the audio signals from the WAV files
    # Replace 'sa.wav' and 'ni.wav' with the paths to your audio files.
    sample_rate_sa, audio_sa = wavfile.read("f1")
    sample_rate_ni, audio_ni = wavfile.read('f2')

    # Step 2: Ensure both signals have the same length
    min_length = min(len(audio_sa), len(audio_ni))
    audio_sa = audio_sa[:min_length]
    audio_ni = audio_ni[:min_length]

    # Step 3: Define mixing weights (gain factors)
    # Adjust the weights to control the mix ratio. For equal mixing, set both to 0.5.
    weight_sa = 0.5  # Weight for 'sa.wav'
    weight_ni = 0.5  # Weight for 'ni.wav'

    # Step 4: Mix the two audio signals mathematically
    mixed_signal = (weight_sa * audio_sa) + (weight_ni * audio_ni)

    # Step 5: Save the mixed audio to a new WAV file
    # Replace 'mixed_output.wav' with the desired output file name.
    wavfile.write('mixed_output.wav', max(sample_rate_sa, sample_rate_ni), mixed_signal.astype(np.int16))


