import simpleaudio as sa
import pretty_midi 
import numpy as np

def pitch_to_freq(pitch):
    return 440 * (2 ** ((pitch - 69) / 12))

def play_generated_notes(generated_notes):
    # Create a PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI()

    # Create an instrument object
    instrument = pretty_midi.Instrument(program=0)

    # Add notes to the instrument
    for index, row in generated_notes.iterrows():
        pitch = int(row['pitch'])
        start_time = row['start']
        end_time = row['end']
        frequency = pitch_to_freq(pitch)
        note = pretty_midi.Note(
            velocity=100,  # Fixed velocity for simplicity
            pitch=pitch,
            start=start_time,
            end=end_time
        )
        instrument.notes.append(note)

    # Add the instrument to the MIDI data
    midi_data.instruments.append(instrument)

    # Write the MIDI data to a file (optional)
    midi_data.write('output.mid')

    # Synthesize the MIDI data and play it
    audio_data = midi_data.synthesize()
    # The audio data is in floating point format, so normalize before converting to 16-bit integers
    audio_data /= np.max(np.abs(audio_data))
    audio_data = (audio_data * 32767).astype(np.int16)

    # Play the audio
    play_obj = sa.play_buffer(audio_data, 1, 2, 44100)

    # Wait for playback to finish
    play_obj.wait_done()

