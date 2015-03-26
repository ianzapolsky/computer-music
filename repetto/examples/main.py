from subprocess import Popen

import abjad
import matplotlib.pyplot as plt
import midi
import numpy as np
import pretty_midi
import random


class MidiPlayer:

    def play_midi_file(self, midi_filename):
        p = Popen(["/Applications/VLC old.app/Contents/MacOS/VLC", "-I", "dummy", midi_filename, "vlc://quit"])


class MidiWriter:

    T             = 0.0
    BEATS_PER_MIN = 120.0
    QUARTER       = 60 / BEATS_PER_MIN
    WHOLE         = QUARTER * 4
    HALF          = QUARTER * 2
    EIGHTH        = WHOLE / 8
    SIXTEENTH     = WHOLE / 16
    THIRTYSECOND  = WHOLE / 32.0

    def __init__(self):
        self.pm = pretty_midi.PrettyMIDI(initial_tempo=self.BEATS_PER_MIN)
        self.pm.instruments.append(pretty_midi.Instrument(1))

    def write_file(self, filename):
        self.pm.write(filename)

    def play_note(self, note, duration, velocity):
        self.pm.instruments[0].notes.append(pretty_midi.Note(velocity, note, self.T, self.T + duration))
        self.T += duration
    
    def play_chord(self, notes, duration, velocity):
        for note in notes:
            self.pm.instruments[0].notes.append(pretty_midi.Note(velocity, note, self.T, self.T + duration))
        self.T += duration
    
if __name__ == '__main__':
    player = MidiPlayer()   
    writer = MidiWriter()

    chord = [60,64,67]
    writer.play_chord(chord, writer.WHOLE, 100)
    writer.write_file('simple.mid')

    player.play_midi_file('simple.mid')
