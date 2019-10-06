from subprocess import Popen


class MidiPlayer:
    def play_midi_file(self, midi_filename):
        p = Popen(["timidity", midi_filename])
