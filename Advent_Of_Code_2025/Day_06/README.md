# 🎄 Day 6: Trash Compactor 🗑️

## 📖 Problem Description

While re-enacting a movie scene with the kitchen Elves, you got a *little* too enthusiastic and jumped into the garbage chute! 😅

Now you're stuck in a trash compactor with a magnetically sealed door! 🚪🔒 Luckily, a family of friendly cephalopods 🐙 approaches - they can open the door, but it'll take time.

While waiting, the youngest cephalopod needs help with her math homework. How hard could cephalopod math be, right? 🤔

---

## 📝 The Math Worksheet

The worksheet lists problems horizontally, but each problem's numbers are arranged **vertically**!

### 🧪 Example:

```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

**How to read it:**
- Numbers are stacked **vertically** in columns
- Operation symbol (`+` or `*`) at the bottom
- Problems separated by **blank columns**
- Alignment within problems doesn't matter

---

## ⭐ Part 1: Left-to-Right Reading

Read the problems from **left to right**, with numbers reading **top to bottom**.

### 🧪 Example Breakdown

**Problem 1** (leftmost):
```
123
 45
  6
  *
```
→ `123 * 45 * 6 = 33210`

**Problem 2:**
```
328
 64
 98
  +
```
→ `328 + 64 + 98 = 490`

**Problem 3:**
```
 51
387
215
  *
```
→ `51 * 387 * 215 = 4243455`

**Problem 4** (rightmost):
```
 64
 23
314
  +
```
→ `64 + 23 + 314 = 401`

**Grand Total:** `33210 + 490 + 4243455 + 401 = 4277556`

### 💡 Strategy
1. Parse columns left-to-right
2. Extract vertical numbers (top-to-bottom)
3. Identify operation from bottom row
4. Calculate each problem's answer
5. Sum all answers

### ✅ Solution
**Grand Total:** `6725216329103`

---

## ⭐⭐ Part 2: Cephalopod Math Revelation! 🐙

Plot twist! The big cephalopods return and explain: **Cephalopod math is written RIGHT-TO-LEFT!** 🔄

Each number is still in its own column, but you read the digits of each number **right-to-left** now!

### 🧪 Same Example, New Reading

```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

Reading **right-to-left**, column by column:

**Problem 1** (rightmost):
```
Column order (R→L): 4, 3, 2, 1
Digit 1: 4    → forms 4
Digit 2: 3    → forms 43
Digit 3: 2    → forms 431
Digit 4: 6    → forms 623 (reading down each column)
```
Wait, let me clarify! Each **column** represents one digit position:
- Rightmost column: ones place
- Next column left: tens place  
- Next column left: hundreds place

So reading the rightmost problem's columns R→L:
- Column 4: `4, 3, 4` → Numbers: `4`, `43`, `431` (reading down)... 

Actually, let me reframe this correctly:

**Reading right-to-left, each column gives digits that form numbers:**
- Rightmost problem columns (R→L): Forms `4 + 431 + 623 = 1058`
- Second from right: `175 * 581 * 32 = 3253600`
- Third from right: `8 + 248 + 369 = 625`
- Leftmost: `356 * 24 * 1 = 8544`

**New Grand Total:** `1058 + 3253600 + 625 + 8544 = 3263827`

### 💡 Strategy
1. Parse columns **right-to-left** instead!
2. Build numbers by reading columns vertically (still top-to-bottom)
3. But process columns in **reverse order**
4. Each column contributes to a different digit position
5. Calculate and sum as before

### ✅ Solution
**Grand Total:** `10600728112865`

---

## 🎯 Key Insights

- 📖 **Part 1:** Standard left-to-right reading (Western style)
- 🔄 **Part 2:** Right-to-left reading (like Arabic/Hebrew!)
- 🐙 **Cultural twist:** Different species, different reading direction!
- 🔢 **Number formation:** Vertical stacking, but column order matters
- 🎲 **Parsing challenge:** Must handle variable-width numbers and spacing
- ⚡ **The catch:** Same data, completely different interpretation!

---

## 🧮 Technical Notes

### Parsing Steps:
1. Split input into rows
2. Identify column positions (character-by-character)
3. Group columns into problems (separated by blank columns)
4. Extract operation symbol from bottom row
5. Build numbers from vertical digits in each column
6. **Part 2:** Reverse column processing order!

### Edge cases:
- Leading/trailing spaces
- Variable number widths
- Alignment variations within columns
- Identifying blank separator columns

---

## 🏆 Challenge Stats

- **Part 1 Answer:** `6725216329103`
- **Part 2 Answer:** `10600728112865`
- **Difficulty:** ⭐⭐⭐⭐☆
- **Concepts:** String parsing, 2D grid reading, directional processing
- **Twist Factor:** 🌪️🌪️🌪️🌪️ (Complete reading reversal!)

---

🐙 *Math homework complete! Now let's get that door open!* 🚪🎄✨
