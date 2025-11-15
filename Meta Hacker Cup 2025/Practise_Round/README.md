# 🍳 Chef's Temperature Challenge

> **Meta Hacker Cup - Practice Problem**

## 📋 Table of Contents
- [Problem Statement](#-problem-statement)
- [Constraints](#-constraints)
- [Input Format](#-input-format)
- [Output Format](#-output-format)
- [Examples](#-examples)
- [Solution Approach](#-solution-approach)
- [Usage](#-usage)
- [Complexity Analysis](#-complexity-analysis)

---

## 🎯 Problem Statement

Chef Alfredo is catering his friend Benji's wedding, and has **N** dishes (numbered from 1 to N) that need to simultaneously go out at specific temperatures. Dish **i** is currently at **Aᵢ** degrees, and must reach a target temperature of exactly **Bᵢ** degrees.

While he has a fancy thermometer, he prefers to rely on his chef instincts to avoid constant measuring. His strategy is to repeatedly apply the following operation:

### 🔥 Operation
Pick two dishes **i** and **j** of different temperatures and **warm up the colder dish** to match the temperature of the hotter dish.

### 🎯 Goal
Find a sequence of at most **N** such operations to get the N dishes to their target temperatures, or determine that it's impossible.

---

## 📊 Constraints

| Parameter | Range |
|-----------|-------|
| Test cases (T) | `1 ≤ T ≤ 95` |
| Number of dishes (N) | `1 ≤ N ≤ 500,000` |
| Current temperature (Aᵢ) | `1 ≤ Aᵢ ≤ N` |
| Target temperature (Bᵢ) | `1 ≤ Bᵢ ≤ N` |

---

## 📥 Input Format

```
T                          # Number of test cases
N                          # Number of dishes
A₁ A₂ ... Aₙ              # Current temperatures
B₁ B₂ ... Bₙ              # Target temperatures
```

**Example:**
```
6
5
1 2 3 4 5
1 2 3 4 5
```

---

## 📤 Output Format

For each test case **i**:
- ✅ **If possible**: `Case #i: K` followed by K operations
- ❌ **If impossible**: `Case #i: -1`

Each operation line contains: `i j` (dish indices)

Where `0 ≤ K ≤ N`

---

## 💡 Examples

### Sample Input
```
6
5
1 2 3 4 5
1 2 3 4 5
3
1 1 2
2 2 2
4
1 2 3 4
3 4 4 4
4
1 2 3 4
1 2 3 3
3
1 3 3
2 2 2
2
1 2
2 1
```

### Sample Output
```
Case #1: 0
Case #2: 2
3 1
3 2
Case #3: 3
3 1
4 2
4 3
Case #4: -1
Case #5: -1
Case #6: -1
```

---

## 📖 Detailed Explanations

### ✅ Test Case 1: Already Perfect
```
Initial: [1, 2, 3, 4, 5]
Target:  [1, 2, 3, 4, 5]
```
🎉 No operations needed!

---

### ✅ Test Case 2: Simple Warming
```
Initial: [1, 1, 2]
Target:  [2, 2, 2]

Operation 1 (3→1): [2, 1, 2]  # Dish 1 warmed to match dish 3
Operation 2 (3→2): [2, 2, 2]  # Dish 2 warmed to match dish 3
```
🎉 Success in 2 operations!

---

### ✅ Test Case 3: Multi-Step Process
```
Initial: [1, 2, 3, 4]
Target:  [3, 4, 4, 4]

Operation 1 (3→1): [3, 2, 3, 4]
Operation 2 (4→2): [3, 4, 3, 4]
Operation 3 (4→3): [3, 4, 4, 4]
```
🎉 Success in 3 operations!

---

### ❌ Test Case 4: Impossible - Decreasing Temperature
```
Initial: [1, 2, 3, 4]
Target:  [1, 2, 3, 3]
```
⚠️ Cannot decrease dish 4 from 4→3!

---

### ❌ Test Case 5: Impossible - Missing Temperature
```
Initial: [1, 3, 3]
Target:  [2, 2, 2]
```
⚠️ Temperature 2 doesn't exist initially!

---

### ❌ Test Case 6: Impossible - Temperature Swap
```
Initial: [1, 2]
Target:  [2, 1]
```
⚠️ Cannot decrease dish 2 from 2→1!

---

## 🧠 Solution Approach

### Key Insights 💡
1. **Cannot decrease temperatures** - only warming is allowed
2. **Target temperatures must exist** in initial configuration
3. **Process by sorted order** for optimal solution

### Algorithm Steps 🔄

```
1. Validation Phase ✓
   ├─ Check: No Bᵢ < Aᵢ (no decreasing)
   └─ Check: All target temps exist in initial config

2. Grouping Phase 📦
   ├─ Group dishes by target temperature
   └─ Track current positions of each temperature

3. Operation Phase 🔥
   ├─ Process temperatures in sorted order
   ├─ For each target temperature:
   │  ├─ Select source dish (already at target)
   │  └─ Warm other dishes to match
   └─ Record all operations

4. Output Phase 📝
   └─ Generate formatted result
```

---

## 🚀 Usage

### Prerequisites
- Python 3.x
- Input file: `input.txt`

### Running the Solution
```bash
python solution.py
```

### File Structure
```
📁 project/
├── 📄 solution.py      # Main solution code
├── 📄 input.txt        # Input test cases
├── 📄 output.txt       # Generated output
└── 📄 README.md        # This file
```

---

## ⚡ Complexity Analysis

| Aspect | Complexity |
|--------|------------|
| **Time Complexity** | O(N log N) per test case |
| **Space Complexity** | O(N) |
| **Operations** | At most N operations |

### Breakdown:
- Sorting temperatures: O(N log N)
- Processing each dish: O(N)
- Total per test case: O(N log N)


</div>
