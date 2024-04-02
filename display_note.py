import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # You also need to 

def plot_piano_roll(notes: pd.DataFrame, count=100):
    if count:
        title = f'First {count} notes'
    else:
        title = f'Whole track'
        count = len(notes['pitch'])
    
    plt.figure(figsize=(8, 4))
    plot_pitch = np.stack([notes['pitch'], notes['pitch']], axis=0)
    plot_start_stop = np.stack([notes['start'], notes['end']], axis=0)
    plt.plot(plot_start_stop[:, :count], plot_pitch[:, :count], color="b", marker=".")
    plt.xlabel('Time [s]')
    plt.ylabel('Pitch')
    plt.title(title)
    plt.grid(True)  # Optionally, add grid lines
    plt.tight_layout()  # Adjust layout
    plt.savefig('piano_roll.png')  # Save the plot as an image

    
