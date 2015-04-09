from player import MidiPlayer
from musician import MidiMusician

if __name__ == '__main__':
    player = MidiPlayer()
    mm = MidiMusician()

    for i in range(51,61):
        mm.add_instrument(i)
    
    for i in range(len(mm.INSTRUMENTS)):
        mm.play_notes_even(i, [mm.C4 for i in range(4)], mm.QUARTER, 100)

    mm.write_file('simple.mid')
    player.play_midi_file('simple.mid')
