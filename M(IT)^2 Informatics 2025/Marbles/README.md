# 🔴🟢🔵 Marbles

Paint marbles so each marble has a different color from the marble it points to.

---

## 🧩 Problem Summary

Busy Beaver lines up N marbles.
Each marble i has a number p_i written on it, with two conditions:

* p is a permutation of 1 through N
* p_i is never equal to i

So every marble points to another marble.
Your task is to assign each marble one of three colors: R, G, or B.
The key requirement is straightforward. Marble i must not share its color with marble p_i.

A valid coloring is guaranteed to exist.

---

## 🎯 Core Idea

Here's the thing. Since p is a permutation with no fixed points, it breaks into cycles.
A cycle always allows a proper coloring with three colors.
Even a 2 cycle or long cycle works with a simple rotation of colors.

Any valid coloring that respects edges i → p_i works.

---

## 📥 Input Format

* First line: integer T
* For each test case:

  * An integer N
  * A list p_1 through p_N forming a permutation with p_i ≠ i

Total N across tests stays within 100000.

---

## 📤 Output Format

For each test case output a string of length N.
Each character must be R, G, or B.
Character i is the color of marble i.

You may output any valid answer.

---

## 🔍 Sample Input

```
5
5
2 1 5 3 4
6
2 1 4 3 6 5
5
2 3 4 5 1
3
3 1 2
4
4 3 2 1
```

## 🔎 Sample Output

```
GBBGR
BGGRRB
RBRBG
RGB
BRGG
```

---

## 💬 Sample Notes

Each case shows a correct coloring where marble i and marble p_i never match colors.
Swapping colors or rotating through R G B also produces valid solutions.

---
