# 🔢 Introduction to Number Theory

Find a positive integer X that relates to every element of the array by divisibility.

---

## 🧩 Problem Summary

You are given an array a of length N.
Your job is to find a positive integer X that respects three conditions:

1. For every i, X is either a multiple of a[i] or a divisor of a[i].
2. There is at least one index where X is a multiple of a[i].
3. There is at least one index where X is a divisor of a[i].

If no such X exists, output −1.

This X does not need to be unique. Any valid answer works.

---

## 🎯 Key Insight

Let's break it down.
The constraints force X to sit in a relationship with every array element through divisibility.
What this really means is that X must be drawn from structure already present in the array.

A practical choice comes from:

* The **gcd** of the entire array
* The **lcm** of some subset
* Or a value between them when both relationships appear across the array

A valid X must satisfy at least one “divides” relationship and one “is divisible by” relationship across different indices, otherwise it fails.

---

## 📥 Input Format

* First line: integer T
* For each test case:

  * An integer N
  * A list of N integers a[1] through a[N]

All a[i] are between 1 and 1e9.
Total N across tests stays within 3⋅10⁵.

---

## 📤 Output Format

For each test case print:

* A single positive integer X if one exists
* Otherwise print −1

If multiple answers work, any is acceptable.

---

## 🔍 Sample Input

```
6
3
36 2 12
6
10 20 30 40 50 60
7
8 7 6 5 4 3 2
6
10 6 1 90 2 15
3
10 2 5
2
1 1
```

## 🔎 Sample Output

```
6
10
-1
30
10
1
```

---

## 💬 Sample Notes

* In the first test, X = 6 divides 36 and 12, and is a multiple of 2.
* In the second test, X = 10 works because it divides every element and is a multiple of 10 at least once.
* In the third test, no X meets both sides of the requirement.

---
