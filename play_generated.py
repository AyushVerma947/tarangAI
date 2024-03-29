from keras.models import load_model
import numpy as np
import tensorflow as tf
import pandas as pd
import simpleaudio as sa

import pretty_midi
key_order=['pitch','step','duration']
print('hi')
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

def predict_next_note(
    notes: np.ndarray,
    model: tf.keras.Model,
    temperature: float = 1.0) -> tuple[int, float, float]:
  """Generates a note as a tuple of (pitch, step, duration), using a trained sequence model."""

  assert temperature > 0

  # Add batch dimension
  inputs = tf.expand_dims(notes, 0)

  predictions = model.predict(inputs)
  pitch_logits = predictions['pitch']
  step = predictions['step']
  duration = predictions['duration']
  print(pitch_logits)
  print(step)
  print(duration)

  pitch_logits /= temperature
  pitch = tf.random.categorical(pitch_logits, num_samples=1)
  pitch = tf.squeeze(pitch, axis=-1)
  duration = tf.squeeze(duration, axis=-1)
  step = tf.squeeze(step, axis=-1)

  # `step` and `duration` values should be non-negative
  step = tf.maximum(0, -step)
  duration = tf.maximum(0, -duration)

  return int(pitch), float(step), float(duration)


def play_gen(pitch,step,duration):
    print('')

    # model=load_model('C:\Users\DELL\OneDrive\Desktop\tarangAI\model_terminal.h5'

# Define the custom loss function
    def mse_with_positive_pressure(y_true: tf.Tensor, y_pred: tf.Tensor):
      mse = (y_true - y_pred) ** 2
      positive_pressure = 10 * tf.maximum(-y_pred, 0.0)
      return tf.reduce_mean(mse + positive_pressure)

    # Register the custom loss function with Keras
    losses = {'mse_with_positive_pressure': mse_with_positive_pressure}

    # Load the model with custom loss function
    model = load_model("C:/Users/DELL/OneDrive/Desktop/tarangAI/model_terminal.h5", custom_objects=losses)

    temperature = 10.0
    num_predictions = 120

    # The initial sequence of notes; pitch is normalized similar to training

    # sequences
    input_notes = (
        [[pitch,step,duration]])
    # print(len(input_notes))
    # print('///////////////////////////////////')
    generated_notes = []
    prev_start = 0
    for _ in range(num_predictions):
        pitch, step, duration = predict_next_note(input_notes, model, temperature)
        start = prev_start + step
        end = start + duration
        input_note = (pitch, step, duration)
        generated_notes.append((*input_note, start, end))
        input_notes = np.delete(input_notes, 0, axis=0)
        input_notes = np.append(input_notes, np.expand_dims(input_note, 0), axis=0)
        prev_start = end
    
    generated_notes = pd.DataFrame(
        generated_notes, columns=(*key_order, 'start', 'end'))
    
    df = generated_notes
    print(generated_notes)
    return generated_notes

