import pretty_midi
import pandas as pd
def notes_to_midi(
  notes: pd.DataFrame,
  out_file: str,
  instrument_name: str,
  velocity: int = 100,  # note loudness
) -> pretty_midi.PrettyMIDI:

  pm = pretty_midi.PrettyMIDI()
  instrument = pretty_midi.Instrument(
      program=pretty_midi.instrument_name_to_program(     # again the pretty midi is converting the notes to midi
          instrument_name))

  prev_start = 0
  for i, note in notes.iterrows():
    start = float(note['start'])
    end = float(note['end'])
    note = pretty_midi.Note(
        velocity=velocity,
        pitch=int(note['pitch']),
        start=start,
        end=end,
    )
    instrument.notes.append(note)
    prev_start = end

  pm.instruments.append(instrument)
  pm.write(out_file)
  return pm