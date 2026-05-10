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
    s32 t;
    cin >> t;
    r(testcase, t) {
        s64 a, b;
        cin >> a >> b;
        s64 g = __gcd(a, b);
        s64 p = b / g;
        s64 q = a / g;
        if (q & 1) cout << "A\n";
        else cout << "B\n";
    }
    return 0;
}