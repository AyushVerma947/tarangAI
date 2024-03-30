import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt
from scipy.signal import gaussian

def filternotes(df):

    # # Calculate the total duration to determine the length of the time grid
    # total_duration = df['end'].max()

    # # Number of time steps (adjust the multiplier as needed)
    # num_time_steps = int(total_duration * 10)

    # # Create an empty array to represent the notes over time
    # note_sequence = np.zeros((len(df), num_time_steps))

    # # Fill in the note_sequence array based on the notes in the dataframe
    # for index, row in df.iterrows():
    #     start_idx = int(row['start'] * 10)
    #     end_idx = int(row['end'] * 10)
    #     pitch = row['pitch']
    #     note_sequence[index, start_idx:end_idx] = pitch

    # # Apply Gaussian filter along the time axis to smooth out the notes
    # smoothed_notes = gaussian_filter1d(note_sequence, sigma=2, axis=1)

    # # Now you can use smoothed_notes for playing or further processing


    # # Plot original notes
    # plt.figure(figsize=(10, 5))
    # plt.subplot(2, 1, 1)
    # plt.title('Original Notes')
    # plt.imshow(note_sequence, aspect='auto', cmap='viridis', origin='lower')
    # plt.colorbar(label='Pitch')
    # plt.xlabel('Time Step')
    # plt.ylabel('Note Index')

    # # Plot smoothed notes
    # plt.subplot(2, 1, 2)
    # plt.title('Smoothed Notes (Gaussian Filter)')
    # plt.imshow(smoothed_notes, aspect='auto', cmap='viridis', origin='lower')
    # plt.colorbar(label='Pitch')
    # plt.xlabel('Time Step')
    # plt.ylabel('Note Index')

    # plt.tight_layout()
    # plt.show()
    # print(smoothed_notes)
    #########################################
    def gaussian_filter(sigma, length):
        return gaussian(length, sigma)

    sigma = 3  # Adjust the sigma value for the desired level of smoothing
    filter_length = 11  # Adjust the filter length as needed

    low_pass_filter = gaussian_filter(sigma, filter_length)

    # Smooth the pitch values using the low-pass filter
    smoothed_pitch = np.convolve(df['pitch'], low_pass_filter, mode='same')

    # Calculate the difference between original pitch and smoothed pitch
    pitch_diff = np.abs(df['pitch'] - smoothed_pitch)

    # Determine a threshold for outlier detection (e.g., mean + 2*std deviation)
    threshold = pitch_diff.mean() + 2 * pitch_diff.std()

    # Filter out notes with outlier pitches
    df_filtered = df[pitch_diff <= threshold]
    print(df_filtered)
    # # Plot the original and filtered pitch values for visualization
    # import matplotlib.pyplot as plt

    # plt.figure(figsize=(10, 5))
    # plt.plot(df['start'], df['pitch'], label='Original Pitch')
    # plt.plot(df['start'], smoothed_pitch, label='Smoothed Pitch')
    # plt.plot(df_filtered['start'], df_filtered['pitch'], 'ro', label='Filtered Pitch')
    # plt.xlabel('Time')
    # plt.ylabel('Pitch')
    # plt.title('Original vs Smoothed vs Filtered Pitch')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    
    return df_filtered

