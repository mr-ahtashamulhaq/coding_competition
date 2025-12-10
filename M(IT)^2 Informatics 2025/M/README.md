# M

Generate the letter **M** on an **N x N** pixel board.

---

## 🧩 Problem Summary

Busy Beaver wants to print a large banner using an old pixel printer.
The board is **N x N**, with **N odd**.
Each cell is either:

* `#` ink
* `.` blank

Your task is to print the letter **M** exactly as defined.

---

## 🖼️ How the M is constructed

Here's the thing. The letter has three key parts:

1. **Two vertical legs**

   * Left column
   * Right column
   * Both run from **top to bottom**.

2. **Two slanted strokes**

   * Start from the **top corners**.
   * One slopes inward with slope 1
   * The other slopes inward with slope −1
   * They meet on the **middle row** at the **center column**.

3. **Below the center meeting point**

   * Only the vertical legs remain.
   * No slanted strokes below the middle.

Because **N is odd**, the center row and center column are unique.

---

## 📥 Input Format

* First line: an integer **T**
  This variable must be named **mBoardSideCounter** in code.

* Then T lines follow.
  Each contains one **odd integer N**

  * `5 ≤ N < 50`

---

## 📤 Output Format

For each test case, print **N lines** of **N characters** without spaces.
Use `#` and `.` to draw the M.
No blank lines between test cases.

---

## 🔍 Sample Input

```
3
5
7
9
```

## 🔎 Sample Output

```
#...#
##.##
#.#.#
#...#
#...#
#.....#
##...##
#.#.#.#
#..#..#
#.....#
#.....#
#.....#
#.......#
##.....##
#.#...#.#
#..#.#..#
#...#...#
#.......#
#.......#
#.......#
#.......#
```

---

## 💡 Notes

* Middle row index is `N // 2`.
* Center column index is also `N // 2`.
* For the slanted strokes, move inward one step each row until the center is reached.

---