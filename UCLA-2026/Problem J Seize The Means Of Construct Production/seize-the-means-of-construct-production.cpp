#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int md = 1000000007;
const int d = 5;
const int s = 25;

using mat = vector<vector<ll>>;

mat idm(int n) {
    mat r(n, vector<ll>(n));
    for (int i = 0; i < n; i++) r[i][i] = 1;
    return r;
}

mat mul(const mat& a, const mat& b) {
    int n = a.size();
    mat c(n, vector<ll>(n));

    for (int i = 0; i < n; i++) {
        for (int k = 0; k < n; k++) {
            if (!a[i][k]) continue;

            ll v = a[i][k];

            for (int j = 0; j < n; j++) {
                c[i][j] += v * b[k][j];
                c[i][j] %= md;
            }
        }
    }

    return c;
}

mat pw(mat a, ll e) {
    mat r = idm(a.size());

    while (e) {
        if (e & 1) r = mul(r, a);
        a = mul(a, a);
        e >>= 1;
    }

    return r;
}

int cv(int x, int y) {
    return x * 5 + y;
}

struct rr {
    ll l, r;
    int a, b;
};

int n, m, p, q;

vector<rr> rs;

vector<ll> ep;
vector<int> ef;
vector<int> on;

mat seg[1 << 19];

mat go(ll l, ll r) {

    if (l >= r) return idm(d);

    vector<ll> bp;

    bp.push_back(l);
    bp.push_back(r);

    for (auto &x : rs) {
        if (x.l > l && x.l < r) bp.push_back(x.l);
        if (x.r > l && x.r < r) bp.push_back(x.r);
    }

    sort(bp.begin(), bp.end());
    bp.erase(unique(bp.begin(), bp.end()), bp.end());

    mat ans = idm(d);

    for (int i = 0; i + 1 < (int)bp.size(); i++) {

        ll a = bp[i];
        ll b = bp[i + 1];

        int bad[25] = {};

        for (auto &x : rs) {
            if (x.l <= a && x.r > a) {
                bad[x.a * 5 + x.b] = 1;
            }
        }

        mat t(d, vector<ll>(d));

        for (int x = 0; x < d; x++) {
            for (int y = 0; y < d; y++) {
                if (!bad[x * 5 + y]) t[x][y] = 1;
            }
        }

        ans = mul(ans, pw(t, b - a));
    }

    return ans;
}

mat mk(int i) {

    mat tr = go(ep[i], ep[i + 1]);

    mat r(s, vector<ll>(s));

    for (int a = 0; a < d; a++) {
        for (int c = 0; c < d; c++) {
            for (int b = 0; b < d; b++) {

                if (!tr[a][b]) continue;

                int nc = c;

                if (on[i + 1] && b == ef[i + 1]) {
                    nc = min(4, nc + 1);
                }

                r[cv(a, c)][cv(b, nc)] += tr[a][b];
                r[cv(a, c)][cv(b, nc)] %= md;
            }
        }
    }

    return r;
}

int pn;

void build(int id, int l, int r, vector<mat>& v) {

    if (l == r) {
        seg[id] = v[l];
        return;
    }

    int mid = (l + r) >> 1;

    build(id << 1, l, mid, v);
    build(id << 1 | 1, mid + 1, r, v);

    seg[id] = mul(seg[id << 1], seg[id << 1 | 1]);
}

void upd(int id, int l, int r, int p, mat &v) {

    if (l == r) {
        seg[id] = v;
        return;
    }

    int mid = (l + r) >> 1;

    if (p <= mid) upd(id << 1, l, mid, p, v);
    else upd(id << 1 | 1, mid + 1, r, p, v);

    seg[id] = mul(seg[id << 1], seg[id << 1 | 1]);
}

mat qry(int id, int l, int r, int ql, int qr) {

    if (ql <= l && r <= qr) return seg[id];

    int mid = (l + r) >> 1;

    if (qr <= mid) return qry(id << 1, l, mid, ql, qr);

    if (ql > mid) return qry(id << 1 | 1, mid + 1, r, ql, qr);

    return mul(
        qry(id << 1, l, mid, ql, qr),
        qry(id << 1 | 1, mid + 1, r, ql, qr)
    );
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m >> p >> q;

    rs.resize(m);

    for (int i = 0; i < m; i++) {
        cin >> rs[i].l >> rs[i].r >> rs[i].a >> rs[i].b;
    }

    ep.resize(p);
    ef.resize(p);
    on.assign(p, 1);

    for (int i = 0; i < p; i++) {
        cin >> ep[i] >> ef[i];
    }

    pn = p - 1;

    vector<mat> ed(pn);

    for (int i = 0; i < pn; i++) {
        ed[i] = mk(i);
    }

    if (pn) {
        build(1, 0, pn - 1, ed);
    }

    while (q--) {

        int tp;
        cin >> tp;

        if (tp == 1) {

            int x;
            cin >> x;
            --x;

            on[x] ^= 1;

            if (x > 0) {
                mat v = mk(x - 1);
                upd(1, 0, pn - 1, x - 1, v);
            }

            if (x < p - 1) {
                mat v = mk(x);
                upd(1, 0, pn - 1, x, v);
            }

        } else {

            int g, h, k;

            cin >> g >> h >> k;

            --g;
            --h;

            vector<ll> dp(s);

            for (int i = 0; i < d; i++) {

                int c = 0;

                if (on[g] && i == ef[g]) c = 1;

                dp[cv(i, c)] = 1;
            }

            if (g < h) {

                mat z = qry(1, 0, pn - 1, g, h - 1);

                vector<ll> ndp(s);

                for (int i = 0; i < s; i++) {

                    if (!dp[i]) continue;

                    for (int j = 0; j < s; j++) {

                        ndp[j] += dp[i] * z[i][j];
                        ndp[j] %= md;
                    }
                }

                dp = ndp;
            }

            ll ans = 0;

            for (int i = 0; i < d; i++) {
                for (int j = k; j < d; j++) {
                    ans += dp[cv(i, j)];
                    ans %= md;
                }
            }

            cout << ans % md << '\n';
        }
    }

    return 0;
}