import random
from midiutil import MIDIFile

#Setup the MIDI file (1 track, time starts at 0)
midi = MIDIFile(1)
midi.addTempo(track=0, time=0, tempo=120)

def note_name(midi_number) :
    names = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

#Finds position in the names list
    name = names[midi_number % 12]

#Calculates the octave
    octave = (midi_number // 12) - 1

    return f"{name}{octave}"

#Define our "pool" of notes
c_scale = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84]
chromatic_scale = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]

durations = [0.5, 1, 2]  # Eighth, quarter, and half notes

current_time = 0


note_or_rest = ["note", "note", "note", "rest"]

def note_decision():
    global decision
    decision = random.choice(note_or_rest)
    return decision

def random_note() :
    note_decision()
    if decision == "note" :
        random_midi = random.choice(c_scale)
        i = note_name(random_midi)
        print (i)
        return (random_midi)
    elif decision == "rest" :
        return ("rest")

def generate_measure(measures) :
    for _ in range(measures):
        bim = 4.0    
        while bim > 0 :
            global length
            length = random.choice(durations)
            if length <= bim :
                global pitch
                pitch = random_note()
                print(f"Note: {pitch} | Length: {length} beats")
            bim = bim - length

def run_randnote() :
    number = int(input("How many notes do you want?"))
    for _ in range(number) :
        print(random_note())

def make_music():
    current_time = 0
    measures = int(input("How many measures would you like to generate?"))
    for _ in range(measures):
        bim = 4.0    
        while bim > 0 :
            length = random.choice(durations)
            if length <= bim :
                pitch = random_note()
            
                if pitch != "rest":
                    midi.addNote(0, 0, pitch, current_time, length, 70)
                    print(f"{note_name(pitch)} | {length}")
                
                print(f"Note: {pitch} | Length: {length} beats")
                
                current_time += length
                bim = bim - length

make_music()

# 4. Save the file
file_name = input("What would you like to name the file?")
with open(f"{file_name}.mid", "wb") as output_file:
    midi.writeFile(output_file)

print(f"file saved as {file_name}.mid!")