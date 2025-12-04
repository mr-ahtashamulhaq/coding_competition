# 🎄 Day 4: Printing Department 🖨️

## 📖 Problem Description

You ride the escalator down to the printing department! 📜 The place is bustling with activity - large rolls of paper everywhere and a massive printer in the corner for those *really big* print jobs! 

The Elves here can make their own decorations (easy!), but you need to keep moving deeper into the North Pole base. There's a cafeteria on the other side of the back wall, but all the forklifts are too busy moving paper rolls around! 🏗️

If you can **optimize the forklift operations**, they might have time to break through the wall! 💪

---

## 🗺️ The Setup

Paper rolls (`@`) are arranged on a large grid. Your input shows their positions:

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

### 🚜 Forklift Access Rule

A forklift can **only access** a roll of paper if it has **fewer than 4 rolls** in its **8 adjacent positions** (including diagonals).

```
. . .
. @ .  ← This roll checks all 8 surrounding cells
. . .
```

---

## ⭐ Part 1: Count Accessible Rolls

Which rolls can the forklifts access right now?

### 🧪 Example

Accessible rolls marked with `x`:

```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

**Answer:** `13` rolls can be accessed

### 💡 Strategy
- Iterate through each roll of paper
- Count neighbors in all 8 directions
- If neighbors < 4, the roll is accessible!

### ✅ Solution
**Accessible rolls:** `1372`

---

## ⭐⭐ Part 2: Chain Reaction Removal! 🔄

Now the real challenge begins! Once you remove accessible rolls, **new rolls might become accessible**!

### 🎯 The Process

1. ✅ Find all accessible rolls (< 4 neighbors)
2. 🗑️ Remove them all
3. 🔁 Repeat until no more rolls can be removed

### 🧪 Example Walkthrough

**Round 1:** Remove 13 accessible rolls
```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

**Round 2:** Remove 12 newly accessible rolls
```
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...
```

**Round 3:** Remove 7 more rolls...

**Continue until...** No more rolls have < 4 neighbors!

**Total Removed:** `13 + 12 + 7 + 5 + 2 + 1 + 1 + 1 + 1 = 43` rolls

### 💡 Strategy
- Simulate the removal process iteratively
- Each round: find all accessible rolls, remove them simultaneously
- Keep going until convergence (no more removals possible)
- Think of it like a **cellular automaton** or **erosion algorithm**

### ✅ Solution
**Total rolls removed:** `7922`

---

## 🎯 Key Insights

- 🔢 **Part 1:** Simple neighbor counting problem
- 🌊 **Part 2:** Cascade/erosion simulation - rolls on the "edge" get removed first
- 🧠 **Parallel removal:** All accessible rolls are removed simultaneously in each round
- 📍 **8-directional neighbors:** Don't forget diagonals!
- 🔄 **Iterative process:** Keep looping until no changes occur
- 🎲 **Edge detection:** Rolls with many neighbors are "protected" until their neighbors are removed

---

## 🧮 Technical Notes

- Grid traversal with 8-directional neighbor checks
- Coordinates: `(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)`
- Boundary handling: cells outside the grid don't count as neighbors
- Part 2 requires multiple passes until stable state
- Similar to: Conway's Game of Life, erosion algorithms, flood fill variants

---

## 🏆 Challenge Stats

- **Part 1 Answer:** `1372`
- **Part 2 Answer:** `7922`
- **Difficulty:** ⭐⭐⭐☆☆
- **Concepts:** Grid traversal, neighbor counting, simulation, cellular automata

---

🚜 *Keep those forklifts busy and break through to the cafeteria!* 🍕🎄✨