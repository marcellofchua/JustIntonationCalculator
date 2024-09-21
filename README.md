This is a Final Project I submitted for Sophia University's "Introduction to Python" course.
It was originally hosted on Replit since the course required that I use Replit for development.
Where it says "Preview | Code | Blame", click on "Code" so you can read this README with the lines numbered.
Jump to Line 55 to understand what my code and project does.
Read Lines 9 to 53 to understand why the currently existing Just Intonation Calculators did not meet my needs.

What makes this Just Intonation Calculator different from other similar projects is the workflow.

THE PROBLEM:
JustIntonate and PlainSound both have their own Just Intonation Calculators,
but they both work in ways that are not useful for fretless guitar players.
I needed a way to calculate Just Intonation where each interval is the same expected frequency,
regardless of which notes are being played or what key you are in.
You can think of it as "converting" an equal tempered key to have justly intonated intervals.
It basically imposes Pythagorean tuning intervals onto what is the A440 Equal Tempered "root note."
This means that my Just Intonation Calculator would be great for "converting" songs that are presumably,
mostly tuned to A440 in equal temperament. I can pick a song in any key, find it's equal tempered root note
relative to A440, and convert it to just intonation.

I needed a Just Intonation Calculator that could convert most songs into Just Intonation relative to the
most common A standard pitch. I'd say, rough estimate, I can get away with using this abstraction 70% of the time,
as a fretless guitarist that needs the root note to stay the same pitch as it is in A440 12TET, but converted to JI.

THE COMPARISON:
JustIntonate's calculator works by dynamically calculating the simplest ratio set for all the given notes present.
This is not useful for fretless guitar players since the frequency of each note changes depending on which notes are present.
This gets messy especially quickly if there's more than 1 instrument playing.
This tool is incredibly cool and I do not fully understand the math or the code, but I need a different soluton for fretless guitars.
Example:
(Guitar Left
A3, C4, and E4 are present.
A3 = 220Hz, C4 = 264Hz, and E4 = 330Hz.)

(Guitar Right
A3, B3, C4, and E4 are present.
A3 = 220Hz, B3 = 248Hz, C4 = 261Hz, and E4 = 330Hz.)
Adding B3 ends up changing the frequency for C4 to make all the notes relative to each other, the simplest ratio set.

(Bass
G3, A3, B3, C4, and E4 are present.
G3 = 196Hz, A3 = 221Hz, B3 = 245Hz, C4 = 261Hz, and E4 = 327Hz.)
Adding G3 ends up changing the frequency to A3, B3, and E4, to make all the notes relative to each other, the simplest ratio set.

Maybe not a realistic example, but if all 3 instruments played their chords listed above at the same time, they would all be out of tune,
relative to each other. The Left Guitarist's C4 and the Right Guitarist's C4 are 3Hz apart.
The Bass's A3, B3, C4, and E4, all differ in varying amounts compared to each guitar part.

PlainSound's calculator works by letting you pick an octave, the pitch, and the relative A4 frequency.
It is much more "clinical" or "academic" in letting you pick the A Pitch Standard.
This is hypothetically the most versatile Just Intonation calculator, but I know that I do not need to
do all this math every single time for every single piece I want to play justly intonated on fretless guitar.
I might not even have all the information I need anyway, to be using this calculator each time.
I need a simpler abstraction that covers the most bases without the workflow being so tedious that I'd rather not use this calculator.

THE SOLUTION:
Ask the user for a root note, the frequency is assumed to be Equal Temperament relative to A440.
Assign the root frequency to the value associated with the root note ET frequency.
For all 12 intervals, multiply the justly intonated ratio by the root note.

Pseudocode. The comments are better in the actual main.py python file.
Store the Equal Temperament Frequencies for A440 in a list.
Store all 12 notes as letters with their accidentals in a list.
Store the names of 12 intervals, excluding octaves, in a list.
Store all 12 justly intonated ratios, excluding octaves, in a list.
Pair the names of the 12 notes with the Equal Tempered frequencies in a dictionary.
Pair the names of the 12 intervals with the Justly Intonated ratios in a dictionary.
Ask user for the root note, which just refers to the Equal Tempered frequency paired to that note.
We now do a rotation to make the letter they chose for the root note to be the 0 index.
Ex: A is 0 by default. If their root note is C, all 12 notes get rotated so that C is 0 instead of 3 which would have been the default.
Validate the input first by checking they chose a note that exists.
If the note exists, then multiply the root frequency by the justly intonated ratios for each interval, and store the associated
note with the interval.
Repeats in a for loop until we go through all notes, prints each Interval with the Justly Intonated Frequency next to the Note.
Add the octave last since it's just root frequency * 2.
