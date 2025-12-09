# 🎄 Day 9: Movie Theater 🎬

## 📖 Problem Description

You slide down the firepole in the corner of the playground and land in the North Pole base movie theater! 🍿✨

The theater has a big tile floor with an interesting pattern. The Elves are redecorating and want to find the **largest rectangle** that uses **red tiles for two opposite corners**! 🔴

---

## 🎨 The Tile Grid

Red tiles are marked with their coordinates:

```
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
```

Visualized (# = red tile, . = other tile):

```
..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............
```

---

## ⭐ Part 1: Largest Rectangle (Any Tiles)

Find the **largest rectangle** using any two red tiles as opposite corners!

The rectangle can include **any tiles** (red or otherwise).

### 🧪 Example Rectangles

**Option 1:** Between `(2,5)` and `(9,7)` → Area = **24**
```
..............
.......#...#..
..............
..#....#......
..............
..OOOOOOOO....
..OOOOOOOO....
..OOOOOOOO.#..
..............
```

**Option 2:** Between `(7,1)` and `(11,7)` → Area = **35**
```
..............
.......OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
.......OOOOO..
..............
```

**Option 3:** Between `(7,3)` and `(2,3)` → Area = **6** (thin!)
```
..............
.......#...#..
..............
..OOOOOO......
..............
..#......#....
..............
.........#.#..
..............
```

**Best:** Between `(2,5)` and `(11,1)` → Area = **50**
```
..............
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..............
.........#.#..
..............
```

### 💡 Strategy

For each pair of red tiles:
1. Calculate rectangle dimensions:
   - Width = `|x₂ - x₁|`
   - Height = `|y₂ - y₁|`
   - Area = Width × Height
2. Track maximum area found

**Optimization:** Only consider tiles that could form valid opposite corners (different x AND different y coordinates).

### ✅ Solution
**Largest rectangle area:** `4755064176`

---

## ⭐⭐ Part 2: Red and Green Tiles Only! 🟢🔴

Plot twist! The Elves remember they can only switch out **red or green** tiles!

### 🌈 The Green Tile Rules

1. **Linear connections:** Each red tile connects to the previous and next red tile with a **straight line of green tiles**
2. **It's a loop:** First red tile connects to last red tile
3. **Adjacent tiles:** Tiles next to each other in the list are always on the same row OR same column
4. **Interior filling:** All tiles **inside the loop** are also green!

### 🧪 Example Green Tiles

Showing green as `X`:

```
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
```

Notice:
- Lines connecting red tiles are green
- Everything inside the closed loop is green
- Tiles outside the loop are neither red nor green

### 🎯 New Constraint

Your rectangle **must only contain red or green tiles**! This is much more restrictive!

### 🧪 Example Rectangles (Red/Green Only)

**Option 1:** Between `(7,3)` and `(11,1)` → Area = **15**
```
..............
.......OOOOO..
.......OOOOO..
..#XXXXOOOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
```

**Option 2:** Between `(9,7)` and `(9,5)` → Area = **3** (vertical line)
```
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXXOXX..
.........OXX..
.........OX#..
..............
```

**Best:** Between `(9,5)` and `(2,3)` → Area = **24**
```
..............
.......#XXX#..
.......XXXXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
.........XXX..
.........#X#..
..............
```

### 💡 Strategy

1. **Build the green tile set:**
   - Connect consecutive red tiles with line segments (green)
   - Use polygon filling algorithm to find interior tiles (green)
   - This forms a closed loop polygon!

2. **For each pair of red tiles:**
   - Check if the rectangle only contains red/green tiles
   - Calculate area if valid
   - Track maximum

3. **Polygon filling:** Use ray casting or scanline algorithm to determine which tiles are inside the polygon

### ✅ Solution
**Largest red/green rectangle area:** `1613305596`

---

## 🎯 Key Insights

- 📐 **Part 1:** Simple geometry - try all pairs of red tiles
- 🔺 **Part 2:** Computational geometry - polygon construction and point-in-polygon testing
- 🎨 **Green tiles form a polygon:** Red tiles are vertices, green tiles fill edges and interior
- 🔍 **Validation needed:** Check every tile in rectangle is red or green
- 📊 **Optimization:** Pre-compute green tile set, use hash set for O(1) lookup
- 🎲 **Loop structure:** The red tiles form a cyclic path around the floor

---

## 🧮 Technical Notes

### Rectangle Area Formula:
```
Width = |x₂ - x₁|
Height = |y₂ - y₁|
Area = Width × Height
```

### Green Tile Generation:
1. **Edge tiles:** Bresenham's line algorithm between consecutive red tiles
2. **Interior tiles:** 
   - Use scanline filling algorithm
   - Or ray casting: count intersections from point to infinity
   - Odd intersections = inside polygon

### Point-in-Polygon Test:
```python
def is_inside_polygon(point, vertices):
    # Ray casting algorithm
    # Cast ray from point to infinity
    # Count edge crossings
    return (crossings % 2) == 1
```

### Validation for Part 2:
```python
def is_valid_rectangle(x1, y1, x2, y2, red_tiles, green_tiles):
    for x in range(min(x1,x2), max(x1,x2)+1):
        for y in range(min(y1,y2), max(y1,y2)+1):
            if (x,y) not in red_tiles and (x,y) not in green_tiles:
                return False
    return True
```

---

## 🏆 Challenge Stats

- **Part 1 Answer:** `4755064176`
- **Part 2 Answer:** `1613305596`
- **Difficulty:** ⭐⭐⭐⭐⭐
- **Concepts:** Computational geometry, polygon filling, point-in-polygon, brute force optimization
- **Geometric Algorithms:** Scanline, ray casting, Bresenham's line

---

🎬 *Floor decorated! Time to catch a movie!* 🍿🎄✨
