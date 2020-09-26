#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

struct LiChaoTree {
    struct Line {
        ll a, b;
        ll f(ll x) {
            return a * x + b;
        }
    };

    struct Node {
        ll s, e;
        Line line;
        int l, r;
    };

    const ll INF = 9223372036854775807LL;
    vector<Node> nodes;

    LiChaoTree(ll s, ll e) {
        nodes.push_back({s, e, {0, INF}, -1, -1});
    }

    void add_line(int i, Line new_line) {
        ll s = nodes[i].s, e = nodes[i].e, m = (s + e) / 2;

        Line low, high;
        if(nodes[i].line.f(s) < new_line.f(s)) {
            low = nodes[i].line;
            high = new_line;
        } else {
            low = new_line;
            high = nodes[i].line;
        }

        // One is above the other.
        if(low.f(e) <= high.f(e)) {
            nodes[i].line = low;
        }
        // Intersect on the right.
        else if(low.f(m) < high.f(m)) {
            nodes[i].line = low;
            if(nodes[i].r == -1) {
                nodes[i].r = nodes.size();
                nodes.push_back({m + 1, e, {0, INF}, -1, -1});
            }
            add_line(nodes[i].r, high);
        }
        // Intersect on the left.
        else {
            nodes[i].line = high;
            if(nodes[i].l == -1) {
                nodes[i].l = nodes.size();
                nodes.push_back({s, m, {0, INF}, -1, -1});
            }
            add_line(nodes[i].l, low);
        }
    }

    ll get_min_y(int i, ll x) {
        if(i == -1) return INF;
        ll s = nodes[i].s, e = nodes[i].e, m = (s + e) / 2;
        if (x <= m)
            return min(nodes[i].line.f(x), get_min_y(nodes[i].l, x));
        else
            return min(nodes[i].line.f(x), get_min_y(nodes[i].r, x));
    }
};

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> dist(n+1), a(n+1, 0), p(n+1), s(n+1);
    for(int i=2; i<=n; i++) cin >> dist[i];
    for(int i=1; i<=n-1; i++) cin >> p[i] >> s[i];

    for(int i=2; i<=n; i++) a[i] = a[i-1] + dist[i];

    LiChaoTree lct(0, 100000000);
    vector<ll> d(n+1);
    d[1] = 0LL;
    for(int i=2; i<=n; i++) {
        lct.add_line(0, {s[i-1], d[i-1]+p[i-1]-(ll)a[i-1]*s[i-1]});
        d[i] = lct.get_min_y(0, a[i]);
    }
    cout << d[n];
}