# 🀄 Mahjong Connect

Determine whether tiles can be partitioned into valid matching pairs.

---

## 🧩 Problem Summary

You are given N tiles on a 2D grid.
Each tile i has:

* position (xᵢ, yᵢ)
* type tᵢ with 1 ≤ tᵢ ≤ M

A pair of tiles (i, j) is considered a **valid match** when all of these hold:

1. They share the same type
2. They lie on the same row or column
3. Every tile strictly between them on that row or column has the same type

Your task is to check whether **all N tiles can be partitioned into N/2 such pairs**.
If yes, output any perfect matching.

---

## 🎯 What this really means

Let’s break it down.

Matching is allowed only inside rows or columns.
Inside each line, tiles of the same type form segments.
Within each segment, tiles can be paired only if the segment size is even.

So the problem becomes:

* Group tiles by (line, type):

  * line is either a row y = constant or a column x = constant
* Within each group, tiles must be matched adjacently because nothing else is allowed without crossing blocked types
* All groups must have even counts for a perfect matching to exist

You simply build segments and check parity.

---

## 📥 Input Format

* First line: N and M
* Next N lines: xᵢ, yᵢ, tᵢ
* All coordinates are bounded by 1e9
* All tiles have distinct positions
* N is even
* 2 ≤ N ≤ 3⋅10⁵

---

## 📤 Output Format

If no perfect matching exists:

```
NO
```

Otherwise:

```
YES
i j
...
```

Print N/2 pairs.
Each tile index must appear exactly once.

---

## 🔍 Sample Input 1

```
4 2
-1 0 1
1 0 1
0 -1 2
0 1 2
```

## 🔎 Sample Output 1

```
YES
1 2
3 4
```

### Why this works

Two type-1 tiles share row y = 0 with nothing blocking.
Two type-2 tiles share column x = 0 with nothing blocking.

---

## 🔍 Sample Input 2

```
4 2
-1 0 1
1 0 1
0 0 2
0 1 2
```

## 🔎 Sample Output 2

```
NO
```

### Explanation

Tiles −1,0 and 1,0 have the same type but tile 0,0 of another type blocks them.

---

## 🔍 Sample Input 3

```
22 3
1 1 2
1 2 2
1 3 2
1 4 1
2 3 2
3 2 1
3 1 2
4 3 2
5 4 1
5 3 1
5 2 1
5 1 1
7 1 3
7 2 3
7 3 3
7 4 3
9 4 3
10 4 3
11 4 3
10 3 1
10 2 1
10 1 3
```

## 🔎 Sample Output 3

```
YES
1 7
2 3
4 9
5 8
6 11
10 12
13 22
14 15
16 17
18 19
20 21
```

---

## 💬 Sample Notes

* Each row and column forms independent matching segments per type
* A perfect matching must pair tiles adjacently inside each segment
* Parity of segment sizes determines feasibility

---