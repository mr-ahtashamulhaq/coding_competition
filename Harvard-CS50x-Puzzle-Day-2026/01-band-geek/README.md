# The Band Geek

## Problem
This puzzle provides a set of scattered musical fragments along with an audio recording of a rehearsal.

We are given:
- Disconnected pieces of sheet music
- A blank staff to reconstruct the composition
- A reference sheet for musical notes

The goal is to reconstruct the correct sequence of the music and extract a final answer from it.

---

## Approach

### 1. Analyze the Audio
The audio announces a sequence of instruments followed by their notes.

Identified order:
- Euphonium  
- Accordion  
- Didgeridoo  
- Euphonium  
- Flute  
- Bassoon  
- Cello  
- Didgeridoo  
- Güiro  

Some instruments repeat, but their **rhythm stays identical even when pitch changes**. This is the key constraint.

---

### 2. Match Audio to Sheet Music
Each instrument corresponds to one sheet music fragment.

Process:
- Identify the starting note for each instrument
- Match it with the correct fragment
- Use rhythm (not pitch) as the primary signal

Important detail:
Repeated instruments (like euphonium and didgeridoo) can swap positions without breaking the solution, since their rhythms match.

---

### 3. Reconstruct the Full Sequence
Arrange all fragments in the same order as the instrument sequence from the audio.

At this point, you have a complete musical line.

---

### 4. Convert Music to Morse Code
The reconstructed rhythm encodes Morse code:

- Long notes → Dash (—)  
- Short notes (eighth notes) → Dot (.)  
- Rests → Letter separators  

Reading the sequence in Morse reveals a phrase.

---

## Solution
GOSPEL ALBUM

---

## Notes
- Rhythm matters more than pitch in this puzzle  
- Audio alignment is the main challenge  
- Once reconstructed, decoding is straightforward using Morse code  