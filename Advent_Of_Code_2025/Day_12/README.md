# 🎄 Day 12: Christmas Tree Farm 🎁

## 📖 Problem Description

You're running out of time! There are no more stairs, elevators, or teleporters... but there IS a ventilation duct! 🌬️

*BUMP BUMP BUMP* - you emerge into a large, well-lit cavern full of Christmas trees! 🌲🌲🌲

The Elves are frantically decorating, but they're worried about fitting all the presents under the trees! It's an ancient tradition, but these presents come in **very weird shapes**! 🎁✨

---

## 🎁 The Present Shapes

Presents are defined as 2D shapes on a grid:

```
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###
```

**Shape notation:**
- `#` = part of the present
- `.` = empty space (not part of the present)

### 🎯 Important Rules:
1. **Rotation and flipping allowed** - presents can be oriented any way
2. **Grid alignment required** - must fit on the unit grid
3. **No overlapping** - `#` from different presents can't occupy the same cell
4. **Can interleave** - `.` spaces don't block other presents!
5. **No stacking** - all presents must fit in 2D

---

## 🌲 The Regions Under Trees

Format: `WIDTHxHEIGHT: count0 count1 count2 ...`

```
4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
```

Example: `12x5: 1 0 1 0 2 2` means:
- Region is **12 units wide × 5 units tall**
- Need to fit:
  - 1 present of shape 0
  - 0 presents of shape 1
  - 1 present of shape 2
  - 0 presents of shape 3
  - 2 presents of shape 4
  - 2 presents of shape 5

---

## ⭐ Part 1: Count Fittable Regions

Determine how many regions can fit **all** their required presents.

### 🧪 Example 1: Region `4x4: 0 0 0 0 2 0`

**Region:** 4×4 grid
```
....
....
....
....
```

**Required:** 2 presents of shape 4
```
Shape 4:
###
#..
###
```

**Solution:** ✅ They fit! Here's one arrangement:
```
AAA.
ABAB
ABAB
.BBB
```
- `A` = first present (shape 4)
- `B` = second present (shape 4, rotated/flipped)

### 🧪 Example 2: Region `12x5: 1 0 1 0 2 2`

**Required:**
- 1 × shape 0
- 1 × shape 2
- 2 × shape 4
- 2 × shape 5

**Solution:** ✅ They all fit!
```
....AAAFFE.E
.BBBAAFFFEEE
DDDBAAFFCECE
DBBB....CCC.
DDD.....C.C.
```

Different letters represent different presents, all fitting perfectly!

### 🧪 Example 3: Region `12x5: 1 0 1 0 3 2`

**Required:**
- 1 × shape 0
- 1 × shape 2
- **3** × shape 4 (one more than example 2!)
- 2 × shape 5

**Solution:** ❌ No way to fit them all!

Even with rotation, flipping, and clever arrangement, that extra shape 4 present just won't fit.

### 📊 Final Count

Out of 3 regions:
- Region 1: ✅ Fits
- Region 2: ✅ Fits
- Region 3: ❌ Doesn't fit

**Answer:** `2` regions can fit all their presents

### 💡 Strategy

This is a **2D bin packing problem** with irregular polyominoes!

**Approach:**
1. **Generate all orientations** of each shape (rotate 90°, 180°, 270°, flip)
2. **Backtracking algorithm:**
   - Try placing each present in all possible positions/orientations
   - If placement is valid (no overlaps), mark those cells as used
   - Recursively place remaining presents
   - If successful, region fits!
   - If not, backtrack and try different position/orientation
3. **Optimization tricks:**
   - Start with largest/most constrained shapes
   - Use bitmasks for fast overlap checking
   - Prune impossible cases early (total area check)

**Key insight:** The `.` in shape definitions means those cells can be shared with other presents!

### ✅ Solution
**Regions that fit all presents:** `454`

---

## 🎯 Key Insights

- 🧩 **Polyomino packing:** Classic NP-complete problem!
- 🔄 **Orientation matters:** Each shape has up to 8 orientations (4 rotations × 2 flips)
- 📦 **Irregular shapes:** Not simple rectangles - complex interlocking
- ⚡ **Backtracking required:** Try all possible placements systematically
- 🎲 **Empty spaces help:** `.` cells allow shapes to nest together
- 🧮 **Constraint satisfaction:** Each region is a CSP to solve
- 🚀 **Optimization crucial:** Without pruning, this is computationally intensive

---

## 🏆 Challenge Stats

- **Part 1 Answer:** `454`
- **Difficulty:** ⭐⭐⭐⭐⭐
- **Concepts:** Polyomino packing, backtracking, constraint satisfaction, NP-complete problems
- **Classic Problem:** 2D bin packing with irregular shapes (like Tetris!)

---

🎁 *Presents perfectly packed! Trees looking festive! Christmas is saved!* 🎄✨🎅
```