# 🎄 Day 1: Secret Entrance 🔐

## 📖 Problem Description

The Elves have discovered project management! 🎉 But there's a catch - they now realize nobody has time to decorate the North Pole! Your mission is to help them by getting through the secret entrance... if only you could remember the password! 🤔

### 🚪 The Setup

You arrive at a mysterious safe with:
- 🎯 A dial numbered **0-99** in a circle
- 📜 A document with rotation instructions
- 🔢 Starting position: **50**

### 🔄 How the Dial Works

The dial rotates in two directions:
- **L** (Left): toward lower numbers
- **R** (Right): toward higher numbers

**Important:** The dial wraps around!
- Going left from `0` → lands on `99`
- Going right from `99` → lands on `0`

#### 📝 Examples:
- At `11`: `R8` → points to `19`
- At `19`: `L19` → points to `0`
- At `5`: `L10` → points to `95`
- At `95`: `R5` → points to `0`

---

## ⭐ Part 1: Count the Endpoints

**The Twist:** The safe is a decoy! 🕵️

The **real password** is the number of times the dial points at **0** after completing any rotation.

### 🧪 Example

```
L68  → 50 to 82
L30  → 82 to 52
R48  → 52 to 0   ✓ (count: 1)
L5   → 0 to 95
R60  → 95 to 55
L55  → 55 to 0   ✓ (count: 2)
L1   → 0 to 99
L99  → 99 to 0   ✓ (count: 3)
R14  → 0 to 14
L82  → 14 to 32
```

**Password:** `3` (dial ended at 0 three times)

### ✅ Solution
**Password:** `1132`

---

## ⭐⭐ Part 2: Method 0x434C49434B

While building a snowman ⛄, you find another document explaining the **newer security protocol**!

Now you must count **every single click** that passes through 0, not just the final positions!

### 🎯 The New Rule

Count 0 when:
1. ✅ The dial **ends** at 0 after a rotation
2. ✅ The dial **passes through** 0 **during** a rotation

### 🧪 Example (Same Rotations)

```
L68  → 50 to 82   (passes 0 once)    ✓
L30  → 82 to 52
R48  → 52 to 0    (ends at 0)        ✓
L5   → 0 to 95
R60  → 95 to 55   (passes 0 once)    ✓
L55  → 55 to 0    (ends at 0)        ✓
L1   → 0 to 99
L99  → 99 to 0    (ends at 0)        ✓
R14  → 0 to 14
L82  → 14 to 32   (passes 0 once)    ✓
```

**Total:** `6` times (3 endpoints + 3 during rotations)

### ⚠️ Watch Out!
A rotation like `R1000` from position `50` would pass through 0 **ten times** before returning to 50!

---

## 🎯 Key Insights

- 🔄 Modular arithmetic is your friend (`% 100`)
- 🧮 Part 1: Count final positions only
- 🔍 Part 2: Count ALL crossings of 0
- 📊 Calculate how many times a rotation crosses 0 based on:
  - Starting position
  - Ending position  
  - Total distance traveled

---

## 🏆 Challenge Stats

- **Part 1 Answer:** `1132`
- **Difficulty:** ⭐⭐⭐☆☆
- **Concepts:** Modular arithmetic, circular arrays, wrapping

---

🎅 *Happy Coding and Merry Christmas!* 🎄✨
```