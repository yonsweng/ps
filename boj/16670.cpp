#include <bits/stdc++.h>

#define MAX 1000001

using namespace std;

pair<int, int> td[300001];
pair<long long, long long> tree[4*MAX];

void init(int node, int tl, int tr) {
    if(tl + 1 == tr) {
        tree[node].second = tl;
        return;
    }
    int mid = (tl + tr) / 2;
    init(node*2, tl, mid);
    init(node*2+1, mid, tr);
}

// Return sum, max.
pair<long long, long long> update(int node, int tl, int tr, int qi, int d) {
    if(qi < tl || tr <= qi) {  // out of range
        return tree[node];
    } else if(tl + 1 == tr) {  // leaf node
        tree[node].first += d;
        tree[node].second += d;
        return tree[node];
    }
    int mid = (tl + tr) / 2;
    pair<long long, long long> left = update(node*2, tl, mid, qi, d);
    pair<long long, long long> right = update(node*2+1, mid, tr, qi, d);
    tree[node].first = left.first + right.first;
    tree[node].second = max(left.second + right.first, right.second);
    return tree[node];
}

long long ans;

void query(int node, int tl, int tr, int qi) {
    if(tr <= qi + 1) {
        ans = max(tree[node].second, ans + tree[node].first);
        return;
    }
    int mid = (tl + tr) / 2;
    query(node*2, tl, mid, qi);
    if(mid <= qi) query(node*2+1, mid, tr, qi);
}

int main() {
    // freopen("1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(NULL);

    init(1, 1, MAX);

    int q;
    cin >> q;

    for(int qi = 1; qi <= q; qi++) {
        char type;
        cin >> type;

        if(type == '+') {
            int t, d;
            cin >> t >> d;

            td[qi].first = t, td[qi].second = d;

            update(1, 1, MAX, t, d);
        } else if(type == '-') {
            int i;
            cin >> i;

            update(1, 1, MAX, td[i].first, -td[i].second);
        } else {
            int t;
            cin >> t;

            ans = 0;
            query(1, 1, MAX, t);

            cout << max(0LL, ans - t) << '\n';
        }
    }
}