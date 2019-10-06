from subprocess import Popen

import numpy as np
import pretty_midi
import random


class MidiPlayer:
    def play_midi_file(self, midi_filename):
        p = Popen(["timidity", midi_filename])


class MidiWriter:

    T = 0.0
    BEATS_PER_MIN = 120.0
    QUARTER = 60 / BEATS_PER_MIN
    WHOLE = QUARTER * 4
    HALF = QUARTER * 2
    QUARTER_TRIP = WHOLE / 6
    EIGHTH = WHOLE / 8
    EIGHTH_TRIP = WHOLE / 12
    SIXTEENTH = WHOLE / 16
    THIRTYSECOND = WHOLE / 32.0

    C1 = 24
    C2 = 36
    C3 = 48
    C4 = 60
    C5 = 72
    C6 = 84
    C7 = 96
    C8 = 108

    def __init__(self):
        self.pm = pretty_midi.PrettyMIDI(initial_tempo=self.BEATS_PER_MIN)
        self.pm.instruments.append(pretty_midi.Instrument(42))

    def write_file(self, filename):
        self.pm.write(filename)

    def play_note(self, instrument, note, duration, velocity, addTime=True):
        self.pm.instruments[instrument].notes.append(
            pretty_midi.Note(velocity, note, self.T, self.T + duration)
        )
        if addTime:
            self.T += duration

    def play_chord(self, instrument, notes, duration, velocity, addTime=True):
        for note in notes:
            self.pm.instruments[instrument].notes.append(
                pretty_midi.Note(velocity, note, self.T, self.T + duration)
            )
        if addTime:
            self.T += duration

    def play_rest(self, duration):
        self.T += duration


if __name__ == "__main__":
    player = MidiPlayer()
    writer = MidiWriter()

    chord = [writer.C3 + 4, writer.C3 + 7, 60, 62, 67, 71]

    for i in range(4):
        for note in chord:
            writer.play_note(0, note, writer.QUARTER, 100)

    writer.write_file("simple.mid")
    player.play_midi_file("simple.mid")
