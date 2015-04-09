import random

from player import MidiPlayer
from musician import MidiMusician

if __name__ == '__main__':
    player = MidiPlayer()   
    mm = MidiMusician()
    mm.add_instrument(42)
    mm.add_instrument(0)
    mm.add_instrument(47)

    for i in range(10):
        note = random.randint(mm.C2, mm.C4)
        stack = mm.fifth_stack(note, 3) + mm.fifth_stack(note + 15, 3)
        mm.play_notes_even(1, stack, mm.EIGHTH_TRIP, 100)
        mm.play_rest(mm.EIGHTH)

    mm.play_notes_even(2, [mm.C4 for i in range(6)], mm.QUARTER_TRIP, 100, False)
    stack = mm.fifth_stack(mm.C4, 3) + mm.fifth_stack(mm.C4 + 15, 3)
    mm.play_chord(1, stack, mm.WHOLE, 100)

    for i in range(10):
        note = random.randint(mm.C2, mm.C4)
        stack = mm.fifth_stack(note, 3) + mm.fifth_stack(note + 16, 3)
        mm.play_notes_even(1, stack, mm.EIGHTH_TRIP, 100)

    mm.play_notes_even(2, [mm.C4 for i in range(6)], mm.QUARTER_TRIP, 100, False)
    stack = mm.fifth_stack(mm.C4, 3) + mm.fifth_stack(mm.C4 + 16, 3)
    mm.play_chord(1, stack, mm.WHOLE, 100)

    for i in range(10):
        note = random.choice(mm.major_scale(mm.C2))
        stack = mm.fifth_stack(note, 3) + mm.fifth_stack(note + 15, 3)
        mm.play_notes_even(1, stack, mm.SIXTEENTH, 100)
        mm.play_rest(mm.EIGHTH)

    mm.play_notes_even(2, [mm.C4 for i in range(6)], mm.QUARTER_TRIP, 100, False)
    stack = mm.fifth_stack(mm.C4, 3) + mm.fifth_stack(mm.C4 + 15, 3)
    mm.play_chord(1, stack, mm.WHOLE, 100)

    for i in range(10):
        note = random.choice(mm.major_scale(mm.C2))
        stack = mm.fifth_stack(note, 3) + mm.fifth_stack(note + 16, 3)
        mm.play_notes_even(1, stack, mm.SIXTEENTH, 100)

    mm.play_notes_even(2, [mm.C4 for i in range(12)], mm.QUARTER_TRIP, 100, False)
    stack = mm.fifth_stack(mm.C4, 3) + mm.fifth_stack(mm.C4 + 16, 3)
    mm.play_chord(1, stack, mm.WHOLE, 100)

    for i in range(10):
        note = random.choice(mm.major_scale(mm.C2))
        stack = mm.fifth_stack(note, 3) + mm.fifth_stack(note + 15, 3)
        mm.play_notes_even(1, stack, mm.THIRTYSECOND, 100)
        mm.play_rest(mm.EIGHTH)

    mm.play_notes_even(2, [mm.C4 for i in range(6)], mm.QUARTER_TRIP, 100, False)
    stack = mm.fifth_stack(mm.C4, 3) + mm.fifth_stack(mm.C4 + 15, 3)
    mm.play_chord(1, stack, mm.WHOLE, 100)

    for i in range(10):
        note = random.choice(mm.major_scale(mm.C2))
        stack = mm.fifth_stack(note, 3) + mm.fifth_stack(note + 16, 3)
        mm.play_notes_even(1, stack, mm.THIRTYSECOND, 100)

    mm.play_notes_even(2, [mm.C4 for i in range(12)], mm.QUARTER_TRIP, 100, False)
    stack = mm.fifth_stack(mm.C4, 3) + mm.fifth_stack(mm.C4 + 16, 3)
    mm.play_chord(1, stack, mm.WHOLE, 100)


    mm.write_file('simple.mid')
    player.play_midi_file('simple.mid')
