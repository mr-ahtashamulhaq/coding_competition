# The Jock

## Problem
This puzzle presents a collection of trading cards featuring fictional players, teams, and achievements.

We are given:
- Player names that appear slightly incorrect
- Associated teams and achievements
- Some cards include jersey numbers, while others do not

The goal is to analyze these inconsistencies and extract a final answer.

---

## Approach

### 1. Identify Real Players from Fake Names
Each name on the cards is one letter off from a real professional athlete.

Example:
- "Gary Hood" → **Gordie Howe**  

Process:
- Match each fake name to a real athlete using the team as a clue  
- Identify the incorrect or missing letter  

Collecting these letters forms a phrase:
WORLD WS CHAMPION → interpreted as **World Series Champion**

---

### 2. Extract Jersey Numbers
For each identified real player:
- Find their jersey number  

One card already provides a number (9), while others require lookup.

Sum of all jersey numbers:
92

---

### 3. Use Achievement Years
Each card also includes a year tied to an achievement.

Compute the average of these years:
1993

---

### 4. Identify the Team
Using the phrase **World Series Champion** along with:

- 92 → indicates 1992  
- 1993 → confirms the following year  

Both years correspond to the same team:

Toronto Blue Jays

---

## Solution
BLUE JAYS

---

## Notes
- The key step is recognizing that names are one letter off real athletes  
- Team names help confirm correct identities  
- Numerical aggregation (sum and average) is used instead of individual mapping  
- Knowledge of World Series history ties everything together  