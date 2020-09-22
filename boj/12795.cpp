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
        nodes.push_back({s, e, {0, -INF}, -1, -1});
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
            nodes[i].line = high;
        }
        // Intersect on the right.
        else if(low.f(m) < high.f(m)) {
            nodes[i].line = high;
            if(nodes[i].r == -1) {
                nodes[i].r = nodes.size();
                nodes.push_back({m + 1, e, {0, -INF}, -1, -1});
            }
            add_line(nodes[i].r, low);
        }
        // Intersect on the left.
        else {
            nodes[i].line = low;
            if(nodes[i].l == -1) {
                nodes[i].l = nodes.size();
                nodes.push_back({s, m, {0, -INF}, -1, -1});
            }
            add_line(nodes[i].l, high);
        }
    }

    ll get_max_y(int i, ll x) {
        if(i == -1) return -INF;
        ll s = nodes[i].s, e = nodes[i].e, m = (s + e) / 2;
        if (x <= m)
            return max(nodes[i].line.f(x), get_max_y(nodes[i].l, x));
        else
            return max(nodes[i].line.f(x), get_max_y(nodes[i].r, x));
    }
};

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr);
    LiChaoTree lct(-1000000000000LL, 1000000000000LL);
    int Q;
    cin >> Q;
    while(Q--) {
        int cmd;
        cin >> cmd;
        if(cmd == 1) {
            ll a, b;
            cin >> a >> b;
            lct.add_line(0, {a, b});
        } else {
            ll x;
            cin >> x;
            cout << lct.get_max_y(0, x) << '\n';
        }
    }
}