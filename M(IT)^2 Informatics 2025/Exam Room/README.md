# 🎓 Exam Room

Count subsets of seats that are “isolated” relative to the origin.

---

## 🧩 Problem Summary

You are given N distinct points P₁ … Pₙ in the plane, none equal to the origin.
Busy Beaver chooses a nonempty subset S of these seats.
The rule is strict:

For every pair Pᵢ, Pⱼ in S with i ≠ j:

```
dist(Pᵢ, Pⱼ) > dist(O, Pᵢ)
```

Each chosen seat must be strictly farther from every other chosen seat than it is from the origin.

Your task is to count how many nonempty subsets satisfy this rule.
Return the answer modulo 998244353.

---

## 🎯 What this really means

Let’s break it down.
Fix a seat Pᵢ. It has radius rᵢ = dist(O, Pᵢ).
Seat Pᵢ cannot coexist with any seat Pⱼ such that dist(Pᵢ, Pⱼ) ≤ rᵢ.

So for each point, you need to understand which other points violate its personal radius rule.
Any valid subset must avoid all such forbidden pairs in both directions.

This becomes a combinatorial counting problem where each point imposes distance constraints shaped by a circle centered at itself with radius equal to its distance from the origin.

---

## 📥 Input Format

* First line: integer N
* Next N lines: coordinates xᵢ, yᵢ
* All points are distinct and nonzero
* Coordinates range from −1e9 to 1e9

---

## 📤 Output Format

A single integer — number of valid nonempty subsets modulo 998244353.

---

## 🔍 Sample Input 1

```
2
1 2
2 1
```

## 🔎 Sample Output 1

```
2
```

### Explanation

Both points are farther from each other than either is from the origin.
So each can be chosen alone, but they cannot coexist.

Valid subsets: {1}, {2}.

---

## 🔍 Sample Input 2

```
3
1 2
2 1
1 -3
```

## 🔎 Sample Output 2

```
5
```

### Explanation

The third point is always safe because its radius is small relative to all pairwise distances.
The first two cannot coexist with each other.
Valid subsets:

* {1}
* {2}
* {3}
* {1, 3}
* {2, 3}

Total: 5.

---