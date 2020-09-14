#include <bits/stdc++.h>

using namespace std;
using ll = long long;

struct Elt {
    int n;
    ll s;
    ll q;
    ll t;
};

vector<vector<pair<int, int>>> adj;

int find_leaf(int here, int parent) {
    if(adj[here].size() == 1)
        return here;

    int leaf = 0;
    for(pair<int, int> p : adj[here]) {
        int there = p.first;
        if(there != parent) {
            leaf = find_leaf(there, here);
            if(leaf)
                break;
        }
    }
    return leaf;
}

Elt dp(int here, int parent) {
    if(adj[here].size() == 1 && parent != 0)
        return {1, 0, 0, 0};

    int na = 0, nb = 1;
    ll sa = 0, sb = 0, qa = 0, qb = 0, la = 0, lb = 0, ta = 0, tb = 0;

    for(pair<int, int> p : adj[here]) {
        int there = p.first, l = p.second;
        if(there != parent) {
            if(na == 0) {
                Elt left = dp(there, here);
                na = left.n;
                sa = left.s;
                qa = left.q;
                ta = left.t;
                la = l;
            } else {
                Elt right = dp(there, here);
                nb = right.n;
                sb = right.s;
                qb = right.q;
                tb = right.t;
                lb = l;
            }
        }
    }

    int nr = na + nb;
    ll sr = sa + sb + na*la + nb*lb;
    ll qr = qa + qb + na*la*la + nb*lb*lb + 2*sa*la + 2*sb*lb;
    ll tr = ta + tb + nb*(qa+na*la*la+2*sa*la) + na*(qb+nb*lb*lb+2*sb*lb) + 2*(sa+na*la)*(sb+nb*lb);
    return {nr, sr, qr, tr};
}

int main() {
    int n;
    cin >> n;

    adj.resize(n+1);

    for(int i=0; i<n-1; i++) {
        int a, b, l;
        cin >> a >> b >> l;
        adj[a].emplace_back(b, l);
        adj[b].emplace_back(a, l);
    }

    // Find a leaf node.
    int root = find_leaf(1, 0);

    Elt result = dp(root, 0);

    cout << result.t;
}