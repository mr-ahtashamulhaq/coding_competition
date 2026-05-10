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
#define r(a, b) for(s32 a = 0; a < (b); a++)
#define rr(a, b) for(s32 a = (b) - 1; a >= 0; a--)
#define il inline
#ifdef RUNFAST
#define ao3 __attribute__ ((optimize(3)))
#endif
#ifndef RUNFAST
#define ao3 __attribute__ ((optimize(0)))
#endif
#define io(a) il a ao3
#define cmp(a, b, c) struct a { public: io(bool) operator() (const b& p1, const b& p2) const { return c(p1, p2); } }
const d64 pi = 3.141592653589793238463L;
const d64 eps = 1e-12;

s32 ao3 main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    s32 n;
    cin >> n;
    vector<vector<u8>> g(n, vector<u8>(n));
    r(i, n) r(j, n) {
        s32 x;
        cin >> x;
        g[i][j] = (u8)x;
    }
    s32 P = n + 2;
    vi df((s64)P * P, 0);
    vi h(n, 0);
    vi zps(n + 1, 0);
    vi sh(n + 2);
    vi sl(n + 2);
    s64 a1 = 0;
    r(i, n) {
        r(j, n) h[j] = g[i][j] ? h[j] + 1 : 0;
        if (i + 1 < n) {
            zps[0] = 0;
            r(j, n) zps[j + 1] = zps[j] + (g[i + 1][j] == 0 ? 1 : 0);
        }
        s32 tp = 0;
        r(j, n + 1) {
            s32 ch = (j == n) ? 0 : h[j];
            s32 cl = j;
            while (tp > 0 && sh[tp - 1] >= ch) {
                s32 th = sh[tp - 1];
                s32 tl = sl[tp - 1];
                tp--;
                if (th > ch) {
                    s32 L = tl;
                    s32 R = j - 1;
                    s32 T = i - th + 1;
                    s32 B = i;
                    bool dm = (i == n - 1) || (zps[R + 1] - zps[L] > 0);
                    if (dm) {
                        a1++;
                        df[(s64)T * P + L]++;
                        df[(s64)T * P + R + 1]--;
                        df[(s64)(B + 1) * P + L]--;
                        df[(s64)(B + 1) * P + R + 1]++;
                    }
                }
                cl = tl;
            }
            if (ch > 0) {
                sh[tp] = ch;
                sl[tp] = cl;
                tp++;
            }
        }
    }
    r(i, P) {
        s64 b = (s64)i * P;
        r(j, P - 1) df[b + j + 1] += df[b + j];
    }
    r(i, P - 1) {
        s64 b = (s64)(i + 1) * P;
        s64 pb = (s64)i * P;
        r(j, P) df[b + j] += df[pb + j];
    }
    vi Q((s64)P * P, 0);
    r(i, n) {
        s64 b = (s64)(i + 1) * P;
        s64 pb = (s64)i * P;
        r(j, n) {
            s32 v = (df[pb + j] == 1) ? 1 : 0;
            Q[b + j + 1] = v + Q[b + j] + Q[pb + j + 1] - Q[pb + j];
        }
    }
    r(j, n) h[j] = 0;
    s64 a2 = 0;
    r(i, n) {
        r(j, n) h[j] = g[i][j] ? h[j] + 1 : 0;
        if (i + 1 < n) {
            zps[0] = 0;
            r(j, n) zps[j + 1] = zps[j] + (g[i + 1][j] == 0 ? 1 : 0);
        }
        s32 tp = 0;
        r(j, n + 1) {
            s32 ch = (j == n) ? 0 : h[j];
            s32 cl = j;
            while (tp > 0 && sh[tp - 1] >= ch) {
                s32 th = sh[tp - 1];
                s32 tl = sl[tp - 1];
                tp--;
                if (th > ch) {
                    s32 L = tl;
                    s32 R = j - 1;
                    s32 T = i - th + 1;
                    s32 B = i;
                    bool dm = (i == n - 1) || (zps[R + 1] - zps[L] > 0);
                    if (dm) {
                        s32 sm = Q[(s64)(B + 1) * P + (R + 1)] - Q[(s64)T * P + (R + 1)] - Q[(s64)(B + 1) * P + L] + Q[(s64)T * P + L];
                        if (sm > 0) a2++;
                    }
                }
                cl = tl;
            }
            if (ch > 0) {
                sh[tp] = ch;
                sl[tp] = cl;
                tp++;
            }
        }
    }
    cout << a1 << ' ' << a2 << '\n';
    return 0;
}
