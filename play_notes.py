import pygame
from music21 import note, stream, tempo

def play_music(notes):
    pygame.init()
    print(notes)

    # Create a stream
    s = stream.Stream()

    # Split the notes by whitespace and create Note objects
    note_list = notes.split()
    for n in note_list:
        n_obj = note.Note(n)
        s.append(n_obj)

    # Set the tempo (adjust as needed)
    s.append(tempo.MetronomeMark(number=120))

    # Save the score as a MIDI file
    s.write('midi', 'output.mid')

    # Load and play the MIDI file using pygame
    pygame.mixer.music.load('output.mid')
    pygame.mixer.music.play()

    # Wait for the music to finish
    pygame.time.wait(int(s.duration.quarterLength * 1000))

    pygame.quit()

# Example usage:
#notes_input = "C4 D4 E4 F4 G4 A4 B4 C5"
#play_music(notes_input)
'''
C C G G A A G    F F E E D D C   G G F F E E D   G G F F E E D   C C G G A A G   F F E E D D C

'''
'''

'''
