# 🎄 Day 3: Lobby 🔋

## 📖 Problem Description

You've made it past security and into the surprisingly vast lobby! 🏢 But there's a problem - all the elevators are offline due to an electrical surge! ⚡😱

An Elf is working on fixing them, but in the meantime, you need to power up the escalator using nearby emergency batteries to reach the printing department below! 📉

### 🔋 The Battery System

Each battery is labeled with a **joltage rating** from `1` to `9`. The batteries are organized into **banks** (one per line in your input).

#### 📊 How It Works:
- Each line = one battery bank
- Turn on **exactly two batteries** per bank
- The joltage produced = the number formed by those two digits
- **Important:** You cannot rearrange batteries! Use them in order.

#### 🧪 Example Bank: `12345`
- Turn on batteries `2` and `4` → produces **24** jolts

---

## ⭐ Part 1: Maximum Joltage with Two Batteries

Find the **largest possible joltage** each bank can produce by selecting exactly **two batteries**.

### 🎯 Example

```
987654321111111  → Max: 98 (first two: 9 and 8)
811111111111119  → Max: 89 (8 and 9)
234234234234278  → Max: 78 (7 and 8 at the end)
818181911112111  → Max: 92 (9 and 2)
```

**Total Output Joltage:** `98 + 89 + 78 + 92 = 357`

### 💡 Strategy
To maximize a 2-digit number:
1. Find the largest digit
2. Find the largest digit that comes **after** it
3. Combine them to form your number

---

## ⭐⭐ Part 2: Joltage Limit Safety Override! 🚨

The escalator still won't move! The Elf hits the big red **"joltage limit safety override"** button (after confirming "yes, I'm sure" many times 😅).

Now you need to turn on exactly **TWELVE batteries** per bank instead of two!

### 🎯 Example (Same Banks)

```
987654321111111  → Max: 987654321111 (skip some 1s at end)
811111111111119  → Max: 811111111119 (skip some 1s)
234234234234278  → Max: 434234234278 (skip 2, 3, 2 near start)
818181911112111  → Max: 888911112111 (skip some 1s near front)
```

**New Total Output Joltage:** 
```
  987654321111
+ 811111111119
+ 434234234278
+ 888911112111
= 3121910778619
```

### 💡 Strategy
To maximize a 12-digit number from a 15-digit bank:
1. You need to **skip exactly 3 batteries**
2. Skip the **smallest** digits possible
3. Skip them as **early** as possible (to keep larger digits in higher place values)
4. Think: Which 3 digits should I **remove** to maximize what remains?

---

## 🎯 Key Insights

- 🔢 **Part 1:** Greedy approach works - find two largest digits in order
- 🧠 **Part 2:** More complex - need to choose which batteries to **skip**
- 📍 **Position matters!** A `9` in the first position is worth more than a `9` at the end
- 🎲 **Strategy shift:** Part 1 is about what to include; Part 2 is about what to exclude
- ⚡ Larger joltage = more power for the escalator!

---

## 🧮 Technical Notes

- Each bank has exactly **15 batteries** (digits)
- Part 1: Select **2** batteries → skip 13
- Part 2: Select **12** batteries → skip 3
- Order must be preserved (no rearranging!)
- Output is a very large number in Part 2 (needs big integer handling)

---

## 🏆 Challenge Stats

- **Difficulty:** ⭐⭐⭐⭐☆
- **Concepts:** Greedy algorithms, digit manipulation, optimization
- **Twist Factor:** 🌪️🌪️🌪️ (Part 2 flips the problem!)

---

🔌 *Power up that escalator and keep decorating!* 🎄✨
