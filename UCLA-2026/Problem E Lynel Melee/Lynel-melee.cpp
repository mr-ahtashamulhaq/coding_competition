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
#define RUNFAST
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

s32 ao3 main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    s32 n, b;
    cin >> n >> b;
    vector<s64> a(n + 1);
    r(i, n) cin >> a[i + 1];
    s64 tot = 0;
    r(i, n) tot += a[i + 1] * max(i + 1, 5);
    s32 m = b + 4;
    s32 z = (m >> 6) + 1;
    vector<u64> dp(z);
    dp[0] = 1;
    s32 lb = m & 63;
    u64 lm = (lb == 63 ? ~0ULL : ((1ULL << (lb + 1)) - 1));
    r(i, n - 4) {
        s64 c = a[i + 5];
        s64 p = 1;
        while (c) {
            s64 k = min(p, c);
            s64 x = k * (i + 5);
            if (x <= m) {
                s32 ax = (s32)x;
                s32 q = ax >> 6;
                s32 w = ax & 63;
                rr(ai, z - q) {
                    u64 v = dp[ai];
                    if (!v)
                        continue;
                    s32 j = ai + q;
                    dp[j] |= v << w;
                    if (w && j + 1 < z)
                        dp[j + 1] |= v >> (64 - w);
                }
                dp[z - 1] &= lm;
            }
            c -= k;
            p <<= 1;
        }
    }
    s64 bs = 0;
    s64 a2 = n >= 2 ? a[2] : 0;
    s64 a3 = n >= 3 ? a[3] : 0;
    s64 a4 = n >= 4 ? a[4] : 0;
    r(li, 4) {
        s32 l = li + 1;
        s32 lim = 4 - l;
        r(c2, min<s64>(a2, lim / 3) + 1) {
            r(c3, min<s64>(a3, (lim - 3 * c2) / 2) + 1) {
                r(c4, min<s64>(a4, lim - 3 * c2 - 2 * c3) + 1) {
                    s32 e = 3 * c2 + 2 * c3 + c4;
                    s32 x = 2 * c2 + 3 * c3 + 4 * c4;
                    s64 h = (s64)b + l - x;
                    if (h >= 0 && h <= m && ((dp[h >> 6] >> (h & 63)) & 1)) {
                        bool g = h > 0 || (c2 && 2 > l) || (c3 && 3 > l) || (c4 && 4 > l);
                        if (g)
                            bs = max(bs, (s64)5 - l - e);
                    }
                }
            }
        }
    }
    cout << tot - b + bs << '\n';
    return 0;
}
