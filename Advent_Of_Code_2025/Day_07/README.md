# 🎄 Day 7: Laboratories 🔬

## 📖 Problem Description

You thank the cephalopods and exit the trash compactor into the research wing of the North Pole base! 🧪

There's a big sign: **"Teleporter Hub"** - naturally, you step onto the large yellow teleporter pad! ⚡✨

*WHOOSH!* You're in an unfamiliar room with no doors! The only exit is the teleporter... which is now leaking magic smoke! 💨😱

Time to fix it! A diagnostic tool displays error code **0H-N0** (oh no!): there's an issue with the tachyon manifold!

---

## ⚙️ The Tachyon Manifold

The manifold is a 2D grid where tachyon beams travel and split:

### 📋 Components:
- **S** = Starting point (beam enters here)
- **.** = Empty space (beam passes through)
- **^** = Splitter (beam splits left and right)

### 🔽 Physics Rules:
1. Tachyon beams always move **downward**
2. Beams pass freely through empty space (`.`)
3. When a beam hits a splitter (`^`):
   - The original beam **stops**
   - Two new beams emit from **immediate left** and **immediate right** of the splitter
   - Both new beams continue downward

---

## ⭐ Part 1: Count the Splits

How many times does the beam split as it travels through the manifold?

### 🧪 Example

```
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
```

**Visualization of beam progression:**

Step 1: Beam reaches first splitter
```
.......S.......
.......|.......
.......^.......  ← Splits here!
```

Step 2: Two beams created
```
......|^|......  ← Left and right beams
```

Step 3: Beams continue and hit more splitters
```
......|.|......
.....|^|^|.....  ← Creates 3 beams (middle shared!)
```

**Final state:**
```
.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|
```

**Total splits:** `21`

### 💡 Strategy
- Simulate beam movement downward
- Track active beam positions
- When beam hits splitter:
  - Count the split
  - Stop that beam
  - Create two new beams (left and right)
- Continue until all beams exit or stop

### ✅ Solution
**Total splits:** `1678`

---

## ⭐⭐ Part 2: Quantum Tachyon Manifold! 🌌

Plot twist! When you open the teleporter, you discover it's not a *classical* manifold - it's a **quantum tachyon manifold**! ⚛️

### 🔮 Quantum Physics Rules:

With quantum mechanics, a **single tachyon particle** takes **BOTH paths** at each splitter!

**Many-Worlds Interpretation:** Each split creates a new timeline:
- Timeline A: Particle went left
- Timeline B: Particle went right

Both timelines exist simultaneously! 🌍🌍

### 🧪 Example Timelines

**Timeline 1:** Always go left
```
.......S.......
.......|.......
......|^.......
......|........
.....|^.^......
.....|.........
....|^.^.^.....
....|..........
...|^.^...^....
...|...........
..|^.^...^.^...
..|............
.|^...^.....^..
.|.............
|^.^.^.^.^...^.
|..............
```

**Timeline 2:** Alternate left/right
```
.......S.......
.......|.......
......|^.......
......|........
......^|^......
.......|.......
.....^|^.^.....
......|........
....^.^|..^....
.......|.......
...^.^.|.^.^...
.......|.......
..^...^|....^..
.......|.......
.^.^.^|^.^...^.
......|........
```

**Timeline 3:** Different path, same endpoint
```
.......S.......
.......|.......
......|^.......
......|........
.....|^.^......
.....|.........
....|^.^.^.....
....|..........
....^|^...^....
.....|.........
...^.^|..^.^...
......|........
..^..|^.....^..
.....|.........
.^.^.^|^.^...^.
......|........
```

**Total unique timelines:** `40`

### 💡 Strategy

Think of it as counting all possible paths through the manifold!

Each splitter encountered **doubles** the number of timelines (mostly):
- If there are `n` timelines and they hit a splitter → creates `2n` timelines

**But beware:** Multiple paths can converge to the same endpoint! Count **unique final positions**, not total paths.

**Better approach:** 
- Track all possible positions the particle could reach
- Use dynamic programming or BFS/DFS
- Count distinct endpoints after all journeys complete
- This is essentially counting all leaf nodes in a binary tree of possibilities!

### ✅ Solution
**Total timelines:** `357525737893560`

That's **357 trillion** timelines! 🤯 The multiverse is vast!

---

## 🎯 Key Insights

- 🔽 **Part 1:** Simple simulation - track beams, count splits
- 🌌 **Part 2:** Combinatorial explosion - exponential growth of timelines!
- 🎲 **Path divergence:** Each splitter creates branching timelines
- 🔄 **Path convergence:** Different routes can lead to same endpoint
- 📊 **Complexity:** Part 2 is essentially counting paths in a DAG (Directed Acyclic Graph)
- ⚛️ **Quantum mechanics:** Every possibility happens in some timeline!

---

## 🧮 Technical Notes

### Part 1 Implementation:
- Queue-based simulation
- Track (x, y) positions of active beams
- Stop beam at splitter, add two new positions
- Count each split event

### Part 2 Implementation:
- **Memoization is key!** Cache states to avoid recalculating
- State = (x, y, path_history) or use position sets
- Count unique endpoints, not paths
- Could use DP: `dp[x][y] = number of ways to reach (x,y)`
- Or BFS/DFS with deduplication

### Edge cases:
- Beams exiting the grid
- Multiple beams at same position
- Infinite loops (shouldn't happen going downward!)

---

## 🏆 Challenge Stats

- **Part 1 Answer:** `1678`
- **Part 2 Answer:** `357525737893560`
- **Difficulty:** ⭐⭐⭐⭐⭐
- **Concepts:** Simulation, path counting, dynamic programming, combinatorics
- **Physics:** Classical vs Quantum mechanics 🔬

---

⚡ *Teleporter fixed! Ready to explore the multiverse!* 🌌🎄✨