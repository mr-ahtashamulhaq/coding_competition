# 🧮 Problem 67

Reconstructing a hidden array through interactive product queries.

---

## 🧩 Problem Summary

Busy Beaver hides an array a of length N.
Each value satisfies 1 ≤ a[i] ≤ 1e9.
There is one special rule: for every pair of elements, they are either coprime or both divisible by 2.

You do not know the array.
You are allowed to query products between pairs of indices.
Your task is to recover all values of the array while using at most 67 queries for full credit.

This is an **interactive** problem.

---

## 🧭 Interaction Rules

Here's the thing.

You may ask a query of the form:

```
? i j
```

The judge replies with a[i] × a[j].
You choose i and j, with i ≠ j.

You must not exceed 100 queries in a test case.
For full points stay within 67.

If you ever receive −1, your solution must stop.
That means you queried incorrectly or exceeded limits.

When you have determined the entire array, output:

```
! a1 a2 ... aN
```

Then proceed to the next test case.

Remember to flush after every query and after the final answer.

---

## 📥 Input Format

* First line: integer T
* For each test case:

  * First line: integer N
  * Interaction begins immediately after reading N

N lies between 5 and 100.
T can go up to 1000.

---

## 📤 Output Protocol

You must:

1. Read N
2. Issue queries with ? i j
3. Use responses to reconstruct the array
4. Output ! followed by the array
5. Continue to the next test case

The final answer does not count toward the query limit.

---

## 🎯 What this really means for solving

The pairwise constraint is important.
Every pair of numbers is either:

* coprime
  or
* both even

This heavily restricts structure. It allows reasoning through gcds and factor relationships when interpreting products.

The array can be determined by strategically sampling pairwise products and exploiting these divisibility patterns.

Because you have at most 67 queries, the solution must avoid scanning the full matrix of pairwise products.

---

## 🔍 Sample Interaction

### Sample Input (judge side)

```
2
5

77

30

85

5

69
```

### Sample Output (solution side)

```
? 1 2
? 3 4
? 4 5
! 7 11 6 5 17

? 1 5
! 1 40 61 41 69
```

### Explanation

In the first test case:

* Query 1: ? 1 2 → 77
* Query 2: ? 3 4 → 30
* Query 3: ? 4 5 → 85
* Final answer: ! 7 11 6 5 17

In the second test case:

* Query: ? 1 5 → 69
* Final answer: ! 1 40 61 41 69

Any valid sequence that reconstructs the array is acceptable.

---