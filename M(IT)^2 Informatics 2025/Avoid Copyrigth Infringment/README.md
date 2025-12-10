# 🧵 Avoid Copyright Infringement

Arrange cards M, I, T with adjacency and pattern restrictions.

---

## 🧩 Problem Summary

Busy Beaver has:

* X cards labeled M
* Y cards labeled I
* Z cards labeled T

He wants to arrange all X + Y + Z cards into a single row.
Two rules guide the arrangement:

1. No two adjacent cards may be equal.
2. No three consecutive cards may form MIT or TIM.

Your task is to decide whether such an arrangement exists.
If it does, output one valid arrangement; otherwise print NO.

---

## 🎯 What this really means

The first rule prevents runs of identical letters.
The second rule blocks two specific forbidden triples that mimic the word MIT in forward or reverse.

So the construction must manage counts carefully, avoid adjacency repetitions, and steer clear of the patterns MIT and TIM.
Greedy ordering with local checks works, provided the counts permit enough alternation.

---

## 📥 Input Format

* First line: integer T
* Each test case: three integers X, Y, Z
* At least one of the counts is nonzero
* Total cards across all tests ≤ 3⋅10⁵

---

## 📤 Output Format

For each test case:

* Print NO if no arrangement satisfies the rules
* Otherwise print YES and then an arrangement string of length X + Y + Z
* Output is case insensitive

---

## 🔍 Sample Input

```
2
1 1 1
3 0 0
```

## 🔎 Sample Output

```
YES
ITM
NO
```

---

## 💬 Sample Notes

* With one of each card, several permutations work because they avoid adjacency issues and never match MIT or TIM.
* With three M cards, the only possible string is MMM, which violates the adjacency rule.

---