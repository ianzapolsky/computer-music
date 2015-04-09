from player import MidiPlayer
from musician import MidiMusician

def minor(mm, note):
    return mm.fifth_stack(note, 3) + mm.fifth_stack(note + 15, 3)

def major(mm, note):
    return mm.fifth_stack(note, 3) + mm.fifth_stack(note + 16, 3)

def augment(note):
    if note != -1:
        return note + 4

if __name__ == '__main__':
    player = MidiPlayer()
    mm = MidiMusician()
    mm.add_instrument(0)

    bass_notes = [mm.C2, mm.C2 + 7, mm.C3, mm.C3 + 4, -1, mm.C3 + 2, -1, mm.C3, -1, mm.C2 + 7]
    maj_chord = mm.fifth_stack(mm.C4, 3) + mm.fifth_stack(mm.C4 + 16, 3)
    min_chord = mm.fifth_stack(mm.C4, 3) + mm.fifth_stack(mm.C4 + 16, 3)

    # play bass_notes
    mm.play_notes_even(0, bass_notes * 8, mm.EIGHTH, 100, False)

    mm.play_rest(mm.QUARTER * 10)
    mm.play_chord(0, major(mm, mm.C4), mm.QUARTER * 5, 100)

    mm.play_rest(mm.QUARTER * 5)
    mm.play_chord(0, major(mm, mm.C4-2), mm.QUARTER * 5, 100)

    mm.play_rest(mm.QUARTER * 5)
    mm.play_chord(0, major(mm, mm.C4), mm.QUARTER, 100)
    mm.play_chord(0, major(mm, mm.C4+1), mm.QUARTER, 100)
    mm.play_chord(0, major(mm, mm.C4), mm.QUARTER * 3, 100)
    mm.play_chord(0, major(mm, mm.C4-2), mm.QUARTER * 5, 100)

    # A flat major
    mm.play_notes_even(0, [-1 if x == -1 else x - 4 for x in bass_notes] * 2, mm.EIGHTH, 100, False)
    mm.play_chord(0, major(mm, mm.C4-4), mm.QUARTER * 5, 100)
    mm.play_rest(mm.QUARTER * 5)

    # back to C major
    mm.play_notes_even(0, bass_notes * 2, mm.EIGHTH, 100, False)
    mm.play_chord(0, major(mm, mm.C4), mm.QUARTER * 5, 100)

    mm.write_file('simple.mid')
    player.play_midi_file('simple.mid')

    
