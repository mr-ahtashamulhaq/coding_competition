# 🎄 Day 10: Factory 🏭

## 📖 Problem Description

Just across the hall from the movie theater, you find a large factory! The Elves here have plenty of time to decorate... because all the factory machines are offline! 😱

Nobody knows the initialization procedure - a Shiba Inu ate that section of the manual! 🐕📖

All that remains are indicator light diagrams, button wiring schematics, and joltage requirements for each machine.

---

## 🔧 The Manual Format

Each machine is described on one line:

```
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
```

- **[square brackets]** = Indicator light diagram
- **(parentheses)** = Button wiring schematics (which lights each button toggles)
- **{curly braces}** = Joltage requirements (ignore for Part 1)

---

## ⭐ Part 1: Configure Indicator Lights 💡

### 📋 How Indicator Lights Work

- `.` = light OFF
- `#` = light ON
- All lights start **OFF**
- Goal: Match the diagram pattern

Example: `[.##.]` means 4 lights, need pattern: OFF-ON-ON-OFF

### 🔘 How Buttons Work

Each button toggles specific lights:
- `(0,3,4)` = Toggles lights 0, 3, and 4 (zero-indexed)
- Toggle means: OFF → ON, ON → OFF
- You push each button an **integer** number of times

### 🧪 Example 1

```
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
```

**Target:** Lights `[.##.]` → positions 1 and 2 ON

**Solution options:**
- Press `(3)`, `(1,3)`, `(2)` once each = **3 presses**
- Press `(1,3)` once, `(2,3)` once, `(0,1)` twice = **4 presses**
- **Optimal:** Press `(0,2)` and `(0,1)` once each = **2 presses** ✅

### 🧪 Example 2

```
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
```

**Target:** Light at position 3 ON

**Optimal:** Press last three buttons once each = **3 presses** ✅

### 🧪 Example 3

```
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
```

**Target:** Lights at positions 1, 2, 3, 5 ON

**Optimal:** Press `(0,3,4)` and `(0,1,2,4,5)` once each = **2 presses** ✅

**Total:** `2 + 3 + 2 = 7` button presses

### 💡 Strategy - Part 1

This is a **system of linear equations over GF(2)** (binary field)!

- Each button press is a variable (how many times to press)
- Each light is an equation (must be ON or OFF)
- Since toggle operations: work modulo 2
- **Only care if button pressed ODD or EVEN number of times**

**Algorithm:**
1. Set up a binary matrix (buttons × lights)
2. Use Gaussian elimination over GF(2)
3. Find minimum solution (fewest 1s in solution vector)
4. This is equivalent to solving a system of XOR equations!

### ✅ Solution
**Minimum button presses:** `512`

---

## ⭐⭐ Part 2: Configure Joltage Levels ⚡

Now the machines are coming online! Time to worry about joltage requirements!

### 🔢 How Joltage Counters Work

- Each machine has multiple counters (one per requirement)
- All counters start at **0**
- Goal: Set counters to match joltage requirements
- Buttons now **increment** counters instead of toggling

Example: `{3,5,4,7}` means:
- Counter 0 → 3
- Counter 1 → 5
- Counter 2 → 4
- Counter 3 → 7

### 🔘 Button Behavior (Joltage Mode)

- `(1,3)` = Increments counters 1 and 3 by 1
- Each button press adds 1 to specified counters
- Push buttons to reach target values

### 🧪 Example 1 (Joltage Mode)

```
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
```

**Target:** Counters `{3,5,4,7}`

**Solution:**
- Press `(3)` × 1 → affects counter 3
- Press `(1,3)` × 3 → affects counters 1 and 3
- Press `(2,3)` × 3 → affects counters 2 and 3
- Press `(0,2)` × 1 → affects counters 0 and 2
- Press `(0,1)` × 2 → affects counters 0 and 1

**Total:** `1 + 3 + 3 + 1 + 2 = 10` presses ✅

### 🧪 Example 2

```
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
```

**Optimal:** **12 presses** ✅

### 🧪 Example 3

```
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
```

**Optimal:** **11 presses** ✅

**Total:** `10 + 12 + 11 = 33` button presses

### 💡 Strategy - Part 2

This is a **system of linear equations over integers**!

- Each button press is a variable (non-negative integer)
- Each counter is an equation (must reach target value)
- Find solution that minimizes total button presses

**Algorithm:**
1. Set up a linear system: Ax = b
   - A = matrix where A[i][j] = 1 if button j affects counter i
   - x = number of times to press each button
   - b = target joltage values
2. Find integer solution minimizing sum of x values
3. This is an **Integer Linear Programming (ILP)** problem!
4. Can use simplex method or branch-and-bound

**Alternative approach:**
- If the button matrix has nice properties, might have closed-form solution
- Check if system is solvable and find minimal solution

### ✅ Solution
**Minimum button presses:** `19857`

---

## 🎯 Key Insights

- 🔀 **Part 1:** Boolean algebra / XOR equations (modulo 2)
- ➕ **Part 2:** Integer linear programming (integer solutions)
- 🧮 **Mathematical transformation:** Same buttons, different arithmetic!
- 📊 **Part 1 is binary:** Only care about parity (odd/even presses)
- 📈 **Part 2 is unbounded:** Need exact counts for each button
- 🎲 **Optimization:** Both parts require minimizing total button presses
- ⚡ **Complexity jump:** Part 2 is NP-hard in general!

---

## 🧮 Technical Notes

### Part 1: Gaussian Elimination (GF(2))
```
1. Build coefficient matrix over binary field
2. Augment with target vector
3. Row reduce to find solution
4. Count 1s in solution vector
```

### Part 2: Integer Linear Programming
```
Minimize: Σ(button_presses)
Subject to:
  - Ax = b (counter targets)
  - x ≥ 0 (non-negative presses)
  - x ∈ ℤ (integer presses)
```

### Key difference:
- **Part 1:** Work modulo 2 (XOR operations)
- **Part 2:** Work over integers (addition operations)

---

## 🏆 Challenge Stats

- **Part 1 Answer:** `512`
- **Part 2 Answer:** `19857`
- **Difficulty:** ⭐⭐⭐⭐⭐
- **Concepts:** Linear algebra, Gaussian elimination, ILP, optimization
- **Math:** GF(2) arithmetic, integer programming, systems of equations

---

🏭 *Factory initialized! Machines humming! Time to get back to decorating!* 🎄✨