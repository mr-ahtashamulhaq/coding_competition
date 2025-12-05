# 🎄 Day 5: Cafeteria 🍽️

## 📖 Problem Description

The forklifts break through the wall and... success! There really *is* a cafeteria on the other side! 🎉

But wait - there's chaos in the kitchen! 👨‍🍳😰 The Elves switched to a new inventory management system right before Christmas, and now they have no idea which ingredients are fresh and which are spoiled!

Time to debug their database! 📊

---

## 🗃️ The Database Format

The database has two sections separated by a blank line:

```
3-5          ← Fresh ingredient ID ranges
10-14
16-20
12-18
             ← Blank line
1            ← Available ingredient IDs to check
5
8
11
17
32
```

### 📋 Rules:
- **Ranges are inclusive:** `3-5` means IDs `3`, `4`, and `5` are all fresh
- **Ranges can overlap:** An ID is fresh if it appears in *any* range
- **Your job:** Check which available IDs are fresh!

---

## ⭐ Part 1: Check Available Ingredients

Given the fresh ranges, determine which of the **available ingredient IDs** are actually fresh.

### 🧪 Example Analysis

```
Fresh ranges: 3-5, 10-14, 16-20, 12-18

ID  1  → ❌ Spoiled (not in any range)
ID  5  → ✅ Fresh (in range 3-5)
ID  8  → ❌ Spoiled (not in any range)
ID 11  → ✅ Fresh (in range 10-14)
ID 17  → ✅ Fresh (in ranges 16-20 AND 12-18)
ID 32  → ❌ Spoiled (not in any range)
```

**Answer:** `3` available IDs are fresh

### 💡 Strategy
- Parse the fresh ID ranges
- For each available ID, check if it falls within any range
- Count how many are fresh

### ✅ Solution
**Fresh available ingredients:** `664`

---

## ⭐⭐ Part 2: Total Fresh ID Count 🔢

The Elves want to know **ALL possible IDs** that the fresh ranges consider to be fresh, regardless of what's currently available!

Now the second section (available IDs) is irrelevant - ignore it completely!

### 🧪 Example

```
Fresh ranges:
3-5
10-14
16-20
12-18
```

**All fresh IDs:**
- From `3-5`: `3, 4, 5`
- From `10-14`: `10, 11, 12, 13, 14`
- From `16-20`: `16, 17, 18, 19, 20`
- From `12-18`: `12, 13, 14, 15, 16, 17, 18` (some overlap!)

**Combined (no duplicates):** `3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20`

**Total count:** `14` unique fresh IDs

### 💡 Strategy

**Naive approach:** Enumerate all IDs ❌ (won't work for huge ranges!)

**Smart approach:** Merge overlapping ranges! ✅
1. Sort ranges by start position
2. Merge overlapping/adjacent ranges
3. Sum the sizes of merged ranges

#### 🔄 Merge Example:
```
Original:  [3-5], [10-14], [16-20], [12-18]
Sorted:    [3-5], [10-14], [12-18], [16-20]
Merged:    [3-5], [10-20]
           └─5-3+1=3   └─20-10+1=11

Total: 3 + 11 = 14
```

### ✅ Solution
**Total fresh ingredient IDs:** `350780324308385`

That's **350 trillion** fresh IDs! 🤯 No wonder they needed range merging!

---

## 🎯 Key Insights

- 🔍 **Part 1:** Simple range checking - is this ID in any range?
- 🧩 **Part 2:** Range merging problem - combine overlapping intervals
- 📈 **Scale jump:** Part 2 has MASSIVE ranges (hence the huge answer)
- 🎲 **Overlap handling:** `[10-14]` and `[12-18]` should merge to `[10-18]`
- ⚡ **Optimization needed:** Can't enumerate 350 trillion IDs individually!

---

## 🧮 Technical Notes

### Range Merging Algorithm:
```
1. Sort ranges by start value
2. Initialize with first range
3. For each subsequent range:
   - If it overlaps with current merged range: extend the end
   - If no overlap: add current to result, start new merged range
4. Count total IDs in all merged ranges
```

### Overlap detection:
- Ranges `[a-b]` and `[c-d]` overlap if: `c <= b + 1`
- Merged range: `[min(a,c) - max(b,d)]`

### Size calculation:
- Range `[a-b]` contains `b - a + 1` IDs

---

## 🏆 Challenge Stats

- **Part 1 Answer:** `664`
- **Part 2 Answer:** `350780324308385`
- **Difficulty:** ⭐⭐⭐⭐☆
- **Concepts:** Range queries, interval merging, set operations
- **Classic problem:** Merge Intervals (LeetCode style!)
---

🥘 *Fresh ingredients secured! Now those wreaths won't hang themselves!* 🎄✨
