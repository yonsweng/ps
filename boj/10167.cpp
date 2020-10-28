#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

struct Point {
    int x, y, w;
    bool operator<(Point &p) {
        return y < p.y || (y == p.y && x < p.x);
    }
};

const int TREE_SIZE = 12000;
ll sum[TREE_SIZE], lmax[TREE_SIZE], rmax[TREE_SIZE], tmax[TREE_SIZE];

void update(int i, int tl, int tr, int q, int v) {
    if(q < tl || tr < q)
        return;

    if(tl == tr) {
        sum[i] += v;
        lmax[i] = max(0LL, sum[i]);
        rmax[i] = max(0LL, sum[i]);
        tmax[i] = max(0LL, sum[i]);
        return;
    }

    int mid = (tl + tr) / 2;
    int l = i * 2, r = i * 2 + 1;
    update(l, tl, mid, q, v);
    update(r, mid+1, tr, q, v);

    sum[i] = sum[l] + sum[r];
    lmax[i] = max(lmax[l], sum[l] + lmax[r]);
    rmax[i] = max(rmax[r], sum[r] + rmax[l]);
    tmax[i] = max(rmax[l] + lmax[r], max(tmax[l], tmax[r]));
}

int main() {
    // freopen("input/1.in", "r", stdin);
    ios::sync_with_stdio(false), cin.tie(nullptr);

    int N;
    cin >> N;

    vector<Point> p(N);
    for(int i=0; i<N; i++)
        cin >> p[i].x >> p[i].y >> p[i].w;

    // Coordinate compression
    vector<int> x(N);
    for(int i=0; i<N; i++)
        x[i] = p[i].x;
    sort(x.begin(), x.end());
    x.erase(unique(x.begin(), x.end()), x.end());
    for(int i=0; i<N; i++)
        p[i].x = lower_bound(x.begin(), x.end(), p[i].x) - x.begin();

    // Sort by y coordinate
    sort(p.begin(), p.end());

    ll answer = 0;
    int prev_y = -1;
    const int MAX_X = int(x.size()) - 1;

    p.resize(N+1);
    p[N].y = 1000000001;

    for(int i=0; i<N; i++) {
        if(prev_y == p[i].y)
            continue;
        prev_y = p[i].y;

        for(int j=i; j<N; j++) {
            update(1, 0, MAX_X, p[j].x, p[j].w);
            if(p[j+1].y != p[j].y)
                answer = max(answer, tmax[1]);
        }

        fill_n(sum, TREE_SIZE, 0LL);
        fill_n(lmax, TREE_SIZE, 0LL);
        fill_n(rmax, TREE_SIZE, 0LL);
        fill_n(tmax, TREE_SIZE, 0LL);
    }

    cout << answer;

    return 0;
}