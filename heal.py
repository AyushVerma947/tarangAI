import numpy as np
import sounddevice as sd
import time
import keyboard

def play_frequency(frequency, duration):
    # Calculate the total number of samples needed
    sample_rate = 44100  # You can adjust this if needed
    num_samples = int(sample_rate * duration)
    
    # Generate a sine wave of the specified frequency
    t = np.linspace(0, duration, num_samples, endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Play the generated sine wave
    sd.play(wave, sample_rate)
    
    # Wait for the specified duration or until the space bar is pressed
    for _ in range(int(duration * 10)):  # Check every 0.1 second
        if keyboard.is_pressed('space'):
            break
        time.sleep(0.1)
    else:
        sd.wait()

    # Set your desired frequency and duration in seconds (dummy values for now)
    # desired_frequency = 261 # in Hertz
    # desired_duration_seconds = 60  # 60 seconds

    # # Play the specified frequency for the specified duration
    # play_frequency(desired_frequency, desired_duration_seconds)