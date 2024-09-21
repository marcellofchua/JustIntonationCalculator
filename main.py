#Frequencies for notes in Equal Temperament A440 stored in a list.
frequencyET = [
    440.00,
    466.16,
    493.88,
    523.25,
    554.37,
    587.33,
    622.25,
    659.25,
    698.46,
    739.99,
    783.99,
    830.61
]

#All 12 notes with accidentals occupying the same index are stored in a list.
notes = [
    'A',
    'A#/Bb',
    'B',
    'C',
    'C#/Db',
    'D',
    'D#/Eb',
    'E',
    'F',
    'F#/Gb',
    'G',
    'G#/Ab']

#All 12 Intervals stored in a list.
intervals = [
    'R1',
    'm2',
    'M2',
    'm3',
    'M3',
    'P4',
    'Tr',
    'P5',
    'm6',
    'M6',
    'm7',
    'M7'
]

#All 12 Just Intonation Ratios stored in a list.
ratios = [
    1,
    16/15,
    9/8,
    6/5,
    5/4,
    4/3,
    7/5,
    3/2,
    8/5,
    5/3,
    16/9,
    15/8
]

#Combine the notes list and frequenciesET list into a dictionary.
#Equal Temperament dictionary that links the 12 notes to the 12 ET frequencies.
NotesET = {}
for key in notes:
    for value in frequencyET:
        NotesET[key] = value
        frequencyET.remove(value)
        break

#Combine the intervals list and ratios list into a dictionary.
#Intervals_Ratios dictionary that links the 12 intervals to the 12 ratios.
#This is needed to calculate the justly intonated frequency of each interval.
intervals_ratios = {}
for key in intervals:
    for value in ratios:
        intervals_ratios[key] = value
        ratios.remove(value)
        break

#Print to show user's their input options.
#Separate the elements of notes by a comma to remove the single quotes.
print(*notes, sep = ', ')
#Ask the user for their root note input.
rootNote = input(str("Select the root note from above: "))

#I need to get the frequency of the rootNote in Equal Temperament.
#We will find a match for rootNote inside NotesET and store that in a variable.
#Since NotesET is a dictionary where the notes are the keys,
#and the frequency is the value,
#I can take the rootNote and find the value associated with the key.
freq = (NotesET[rootNote])

#We need the index of rootNote in notes to rotate the notes list.
#Example: The note A is at index 0 by default.
#If the user selects note B as their rootNote, we change the index of B to 0.
index = notes.index(rootNote)
#We store the rotated notes list in a variable called 'rotatedNotes'.
rotatedNotes = [notes[(i + index) % len(notes)] for i, x in enumerate(notes)]

#validate input, needs to be a note that exists
if rootNote in NotesET:
    #combine intervals (key) and frequencies (values) into a list
    intervals_frequencies = []
    for key, value in intervals_ratios.items():
        y = (f'{key} = {round(value*freq)}Hz')
        intervals_frequencies.append(y)
    #combine these two lists into a new dictionary
    #this was the only way I figured out how to print 3 elements on the same line
    notes_intervals_frequencies = {}
    for key in intervals_frequencies:
        for value in rotatedNotes:
            notes_intervals_frequencies[key] = value
            rotatedNotes.remove(value)
            break
    for key, value in notes_intervals_frequencies.items():
        print(key, value)
else:
    print(f'{rootNote} is not a note, please enter a note')

#print octave calculated from root
octave = freq*2
print(f'O1 = {round(octave)}Hz' + f' {rootNote}')
