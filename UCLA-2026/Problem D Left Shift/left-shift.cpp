#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <ranges>
#include <unordered_set>
#include <unordered_map>
#include <stdfloat>
using namespace std;
#define s8 int8_t
#define s16 short
#define s32 int
#define s64 long long
#define s128 __int128
#define u8 uint8_t
#define u16 unsigned short
#define u32 unsigned int
#define u64 unsigned long long
#define u128 unsigned __int128
#define d32 float
#define d64 long double
#define d128 float128_t
#define ii pair<s32, s32>
#define vi vector<s32>
#define vii vector<ii>
#define vvi vector<vi>
#define vvii vector<vii>
#define r(a, b) for (s32 a = 0; a < (b); a++)
#define rr(a, b) for (s32 a = (b) - 1; a >= 0; a--)
#define il inline
#ifdef RUNFAST
#define ao3 __attribute__((optimize(3)))
#endif
#ifndef RUNFAST
#define ao3 __attribute__((optimize(0)))
#endif
#define io(a) il a ao3
#define cmp(a, b, c) struct a { public: io(bool) operator() (const b& p1, const b& p2) const { return c(p1, p2); } }
const d64 pi = 3.141592653589793238463L;
const d64 eps = 1e-12;

s32 ans;
s32 bl = -1;
s32 br = -1;
s32 e[2005][2005];

io(bool) isp(s32 l, s32 r2) {
    if (l >= r2)
        return true;
    s32 z = r2 - l + 1;
    return e[l][r2] >= z / 2;
}

io(void) up(s32 q, s32 l, s32 r2) {
    if (q >= 2 && q > ans) {
        ans = q;
        if (l < 0 || l == r2) {
            bl = -1;
            br = -1;
        } else {
            bl = l;
            br = r2;
        }
    }
}

s32 ao3 main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    s32 n;
    cin >> n;
    string a;
    cin >> a;
    string s = " " + a;
    static s32 o[2005][2005];
    static s32 nx[2005][26];
    static s32 pr[2005][26];
    for (s32 i = n; i >= 1; i--) {
        for (s32 j = 1; j <= n; j++) {
            if (s[i] == s[j])
                e[i][j] = e[i + 1][j - 1] + 1;
            else
                e[i][j] = 0;
        }
    }
    for (s32 i = 1; i <= n; i++) {
        for (s32 j = n; j >= 1; j--) {
            if (s[i] == s[j])
                o[i][j] = o[i - 1][j + 1] + 1;
            else
                o[i][j] = 0;
        }
    }
    r(c, 26) nx[n + 1][c] = n + 1;
    for (s32 i = n; i >= 1; i--) {
        r(c, 26) nx[i][c] = nx[i + 1][c];
        nx[i][s[i] - 'a'] = i;
    }
    for (s32 i = 1; i <= n; i++) {
        r(c, 26) pr[i][c] = pr[i - 1][c];
        pr[i][s[i] - 'a'] = i;
    }
    for (s32 len = 2; len <= n; len += 2) {
        s32 h = len / 2;
        for (s32 i = 1; i + len - 1 <= n; i++) {
            s32 j = i + len - 1;
            s32 p = e[i][j];
            if (p > h)
                p = h;
            if (p >= h) {
                up(len, -1, -1);
            } else {
                s32 sf = o[i + h - 1][i + h];
                if (sf > h)
                    sf = h;
                s32 x = p + 1;
                s32 y = h - sf;
                if (x < y && s[i + x - 1] == s[j - y + 1] && e[i + x][j - x + 1] >= y - x) {
                    up(len, i + x - 1, i + y - 1);
                }
            }
            if (h >= 2 && s[i + h] == s[i + h + 1]) {
                s32 dl = h - 2;
                s32 p1 = e[i][j];
                if (p1 > dl)
                    p1 = dl;
                s32 f;
                if (p1 >= dl)
                    f = h - 1;
                else
                    f = p1 + 1;
                s32 c = s[i + f - 1] - 'a';
                s32 m = h - f;
                s32 l2 = m - 1;
                s32 p2 = 0;
                s32 s2 = 0;
                if (l2 > 0) {
                    p2 = e[i + f][j - f + 1];
                    if (p2 > l2)
                        p2 = l2;
                    s2 = o[i + h - 1][i + h + 2];
                    if (s2 > l2)
                        s2 = l2;
                }
                s32 lo = m - s2;
                s32 hi = p2 + 1;
                if (lo <= hi) {
                    s32 aa = i + f + lo - 1;
                    s32 bb = i + f + hi - 1;
                    s32 z = nx[aa][c];
                    if (z <= bb) {
                        s32 zr = z - i + 1;
                        up(len, i + f - 1, i + 2 * h - zr + 1);
                    }
                }
            }
        }
    }
    for (s32 len = 3; len <= n; len += 2) {
        s32 h = len / 2;
        for (s32 i = 1; i + len - 1 <= n; i++) {
            s32 j = i + len - 1;
            s32 p = e[i][j];
            if (p > h)
                p = h;
            if (p >= h) {
                s32 d = i + h;
                up(len - 1, d, j);
            } else {
                s32 x = i + p;
                s32 y = j - p;
                if (isp(x + 1, y))
                    up(len - 1, x, j);
                if (isp(x, y - 1)) {
                    if (y < j)
                        up(len - 1, y, j);
                    else
                        up(len - 1, -1, -1);
                }
            }
        }
    }
    for (s32 len = 1; len <= n; len += 2) {
        s32 h = len / 2;
        for (s32 i = 3; i + len - 1 <= n; i++) {
            s32 j = i + len - 1;
            s32 p = e[i][j];
            if (p > h)
                p = h;
            if (p >= h) {
                s32 md = i + h;
                s32 c = s[md] - 'a';
                s32 l = pr[i - 2][c];
                if (l)
                    up(len + 1, l, md - 1);
            } else {
                s32 x = i + p;
                s32 y = j - p;
                s32 c = s[x] - 'a';
                s32 l = pr[i - 2][c];
                if (l && isp(x + 1, y))
                    up(len + 1, l, y);
                c = s[y] - 'a';
                l = pr[i - 2][c];
                if (l && isp(x, y - 1))
                    up(len + 1, l, x - 1);
            }
        }
    }
    if (ans == 0) {
        cout << -1 << '\n';
    } else {
        cout << ans << '\n';
        if (bl == -1)
            cout << -1 << '\n';
        else
            cout << bl << ' ' << br << '\n';
    }
    return 0;
}
