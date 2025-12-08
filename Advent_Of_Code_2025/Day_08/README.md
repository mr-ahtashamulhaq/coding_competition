# 🎄 Day 8: Playground 🎪

## 📖 Problem Description

You step onto the repaired teleporter and *WHOOSH* - you rematerialize in a vast underground space containing a **giant playground**! 🎠✨

Across the playground, Elves are working on an ambitious Christmas decoration project. They've suspended numerous small electrical junction boxes in 3D space and plan to connect them with strings of lights! 💡

### ⚡ The Electrical System

- Most junction boxes don't provide electricity themselves
- When two boxes are connected, electricity flows between them
- Connected boxes form a **circuit**
- Goal: Connect boxes so electricity reaches everywhere!

---

## 📍 The Setup

You're given a list of junction box positions in **3D space**:

```
162,817,812  ← X=162, Y=817, Z=812
57,618,57
906,360,560
592,479,940
352,342,300
...
```

Each line represents one junction box with `X,Y,Z` coordinates.

### 📏 Distance Calculation

Use **straight-line (Euclidean) distance** in 3D:

```
distance = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]
```

---

## ⭐ Part 1: Connect 1000 Closest Pairs

The Elves want to save on string lights by connecting the **closest pairs** first!

### 🔧 The Algorithm

1. Find the two junction boxes with the shortest distance between them
2. Connect them (they join the same circuit)
3. Find the next two **unconnected** boxes that are closest
4. Connect them
5. Repeat...

**Important:** If two boxes are already in the same circuit, connecting them does nothing!

### 🧪 Example Walkthrough

Starting with 20 junction boxes:

**Connection 1:** `162,817,812` ↔ `425,690,689` (closest pair)
- Result: 1 circuit with 2 boxes, 18 circuits with 1 box each

**Connection 2:** `162,817,812` ↔ `431,825,988`
- Since `162,817,812` is already connected to `425,690,689`, all three merge!
- Result: 1 circuit with 3 boxes, 17 circuits with 1 box each

**Connection 3:** `906,360,560` ↔ `805,96,715`
- Result: 1 circuit with 3 boxes, 1 circuit with 2 boxes, 15 individual boxes

**Connection 4:** `431,825,988` ↔ `425,690,689`
- Both already in same circuit → **Nothing happens!**

After **10 shortest connections:**
- 1 circuit with **5** boxes
- 1 circuit with **4** boxes  
- 2 circuits with **2** boxes each
- 7 circuits with **1** box each

**Answer:** Multiply three largest circuit sizes → `5 × 4 × 2 = 40`

### 💡 Strategy

This is **Kruskal's Minimum Spanning Tree** algorithm with a twist!

- Use **Union-Find** (Disjoint Set Union) to track circuits
- Sort all pairs by distance (or use priority queue)
- Connect pairs in order of distance
- Track circuit sizes
- After 1000 connections, find three largest circuits

### ✅ Solution

After connecting the **1000 closest pairs**:

**Answer:** `105952` (product of three largest circuit sizes)

---

## ⭐⭐ Part 2: Unite Them All! 🌐

The Elves don't have enough extension cables! You need to keep connecting until **all junction boxes form ONE circuit**!

### 🎯 The Goal

Find the **last connection** that unites everything into a single circuit.

### 🧪 Example

Continuing from above, the connection that finally unites all 20 boxes is:
- `216,146,977` ↔ `117,168,530`

To find the right extension cable length, multiply their **X coordinates**:
- `216 × 117 = 25272`

### 💡 Strategy

Continue Kruskal's algorithm until there's only **1 circuit** remaining:
- Keep connecting closest unconnected pairs
- Use Union-Find to detect when only one component remains
- Track the last two boxes that were connected
- Return the product of their X coordinates

### ✅ Solution

**Last connection X-coordinate product:** `975931446`

---

## 🎯 Key Insights

- 🌲 **Part 1:** Partial Minimum Spanning Forest (1000 edges)
- 🌳 **Part 2:** Complete Minimum Spanning Tree (unite all)
- 🔗 **Union-Find is essential:** Efficiently track connected components
- 📊 **Edge sorting:** Pre-sort all O(n²) pairs by distance
- ⚡ **Optimization:** Only compute distances once, store in priority queue
- 🎲 **Circuit merging:** When connecting boxes in different circuits, merge them!

---

## 🧮 Technical Notes

### Union-Find (Disjoint Set Union):
```
- find(x): Find the root/representative of x's circuit
- union(x, y): Merge circuits containing x and y
- size(x): Track size of circuit containing x
```

### Algorithm Steps:
1. Calculate all pairwise distances: O(n²)
2. Sort edges by distance: O(n² log n)
3. Process edges in order:
   - Check if endpoints in same circuit
   - If not, connect them and merge circuits
4. Track circuit sizes throughout

### Distance Calculation:
```python
def distance_3d(p1, p2):
    return sqrt((p1.x - p2.x)² + (p1.y - p2.y)² + (p1.z - p2.z)²)
```

### Circuit Counting:
- After each union, count distinct root nodes
- Part 1: Stop after 1000 connections
- Part 2: Stop when only 1 root remains

---

## 🏆 Challenge Stats

- **Part 1 Answer:** `105952`
- **Part 2 Answer:** `975931446`
- **Difficulty:** ⭐⭐⭐⭐☆
- **Concepts:** Minimum Spanning Tree, Union-Find, 3D geometry, Kruskal's Algorithm
- **Classic Algorithm:** MST with a creative twist!

---

💡 *All junction boxes connected! Let there be light!* ✨🎄🔌