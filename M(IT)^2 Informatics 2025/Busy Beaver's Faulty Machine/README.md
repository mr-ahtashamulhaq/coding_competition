# 🧮 Busy Beaver’s Faulty Machine

Rebuild Y and Z so they share digits and satisfy X + Y = Z.

---

## 🧩 Problem Summary

You are given an integer X in base B as a digit sequence without leading zeroes.
Your task is to decide whether there exist two positive integers Y and Z such that:

1. X + Y = Z
2. Y and Z use exactly the same multiset of digits
3. Neither Y nor Z has leading zeroes
4. Both have fewer than 2⋅10⁵ digits

If such Y and Z exist, output them.

---

## 🎯 What this really means

Here’s the thing.
The equation X + Y = Z means Y and Z differ by exactly X.
Yet their digit multisets match, which forces a tight structural relationship.
You need to construct a digit sequence p for Y and a digit sequence q for Z using the same multiset, keeping q = p + X in base B.

A constructive solution needs to manage carries carefully while ensuring both numbers remain valid digit permutations.

In many cases this is possible by:

* Taking a multiset large enough to absorb X
* Reordering digits to align with X’s magnitude
* Controlling carry propagation so q and p stay within digit limits

If the constraints block all valid constructions, output NO.

---

## 📥 Input Format

* First line: integer T
* For each test case:

  * Two integers N and B
  * A line of N digits a₁ … aₙ representing X in base B
* No leading zeroes
* Total N across all tests ≤ 2⋅10⁵

---

## 📤 Output Format

For each test case:

If no Y and Z exist:

```
NO
```

Otherwise print:

```
YES
M
p₁ p₂ … pₘ
q₁ q₂ … qₘ
```

Where:

* M is the number of digits in Y and Z
* Both sequences use the same multiset of digits
* Both represent positive integers with no leading zero
* They satisfy X + Y = Z

---

## 🔍 Sample Input

```
3
2 10
3 6
4 5
1 4 3 4
5 12
4 8 8 3 1
```

## 🔎 Sample Output

```
YES
2
1 5
5 1
YES
4
1 4 3 2
3 4 2 1
NO
```

---

## 💬 Sample Notes

* For X = 36 base 10, Y = 15 and Z = 51 share digits {1,5} and satisfy X + Y = Z.
* For X = 244 base 5, a valid choice is Y = 242 and Z = 486 represented with digits {1,2,3,4}.
* Some cases cannot match the digit multiset constraint and must return NO.

---