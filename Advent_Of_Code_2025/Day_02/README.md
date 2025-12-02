# 🎁 Day 2: Gift Shop

## Problem Summary

You've made it to the gift shop at the North Pole! However, a mischievous young Elf has been playing around with the gift shop computer and added a bunch of **invalid product IDs** to the database. Your mission is to identify and sum up all these invalid IDs from the given ranges.

The catch? The Elf was creating silly patterns by repeating digit sequences, and you need to find all IDs that match these patterns! 🔍

---

## 📋 Part One: Double Repetition

An ID is **invalid** if it's made up of some sequence of digits repeated **exactly twice**.

### Examples of Invalid IDs:
- `55` → `5` repeated 2 times
- `6464` → `64` repeated 2 times  
- `123123` → `123` repeated 2 times

### Examples of Valid IDs:
- `101` → valid (no repeating pattern)
- `1010` → ❌ this is `10` twice, so it's invalid!

### Sample Input:
```
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
```

### Sample Output:
Expected sum: **1227775554**

#### Breakdown:
| Range | Invalid IDs | Count |
|-------|-------------|-------|
| `11-22` | 11, 22 | 2 |
| `95-115` | 99 | 1 |
| `998-1012` | 1010 | 1 |
| `1188511880-1188511890` | 1188511885 | 1 |
| `222220-222224` | 222222 | 1 |
| `1698522-1698528` | *(none)* | 0 |
| `446443-446449` | 446446 | 1 |
| `38593856-38593862` | 38593859 | 1 |
| `565653-565659` | *(none)* | 0 |
| `824824821-824824827` | *(none)* | 0 |
| `2121212118-2121212124` | *(none)* | 0 |

---

## 🚀 Part Two: Multiple Repetitions

The plot thickens! 🎭 Now an ID is **invalid** if it's made up of some sequence of digits repeated **at least twice** (2, 3, 4, or more times).

### Examples of Invalid IDs:
- `12341234` → `1234` repeated 2 times
- `123123123` → `123` repeated 3 times
- `1212121212` → `12` repeated 5 times
- `1111111` → `1` repeated 7 times
- `111` → `1` repeated 3 times ⚠️ (new!)

### Updated Sample Output:
Expected sum: **4174379265**

#### Updated Breakdown:
| Range | Invalid IDs | Change |
|-------|-------------|--------|
| `11-22` | 11, 22 | — |
| `95-115` | 99, **111** | ✨ added 111 |
| `998-1012` | 999, 1010 | ✨ added 999 |
| `1188511880-1188511890` | 1188511885 | — |
| `222220-222224` | 222222 | — |
| `1698522-1698528` | *(none)* | — |
| `446443-446449` | 446446 | — |
| `38593856-38593862` | 38593859 | — |
| `565653-565659` | **565656** | ✨ added 565656 |
| `824824821-824824827` | **824824824** | ✨ added 824824824 |
| `2121212118-2121212124` | **2121212121** | ✨ added 2121212121 |

---

## 🔑 Key Insights

✅ **No leading zeros** - `0101` is not a valid ID format  
✅ **Pattern detection** - The key is identifying if an ID can be formed by repeating a substring  
✅ **Range iteration** - Efficiently check all IDs within each given range  
✅ **Pattern validation** - A substring repeated k times equals the full number length

---

## 🧩 Solution Approach

1. Parse the input to extract all ranges
2. For each range, iterate through all IDs
3. For each ID, check if it's invalid by:
   - **Part One**: Testing if the ID is exactly the first half repeated twice
   - **Part Two**: Testing if the ID can be formed by repeating any substring at least twice
4. Sum all invalid IDs found

---

## 📝 Notes

- Remember to handle large numbers efficiently
- Consider the substring length divisors when checking for patterns
- The ranges can be very large, so optimization matters!

Good luck, and happy pattern hunting! 🎄✨